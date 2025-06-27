import subprocess
import time
import sys
import os
from datetime import datetime
import platform

def shutdown_pc():
    """Shutdown the PC based on the operating system"""
    system = platform.system().lower()
    
    print(f"\n🖥️  Shutting down PC in 30 seconds...")
    print(f"⚠️  Press Ctrl+C to cancel shutdown")
    
    try:
        # Give user 30 seconds to cancel
        for i in range(30, 0, -1):
            print(f"⏰ Shutdown in {i} seconds...", end='\r')
            time.sleep(1)
        
        print(f"\n🔄 Shutting down now...")
        
        if system == "windows":
            os.system("shutdown /s /t 0")
        elif system == "linux" or system == "darwin":  # Linux or macOS
            os.system("shutdown -h now")
        else:
            print(f"❌ Unsupported operating system: {system}")
            
    except KeyboardInterrupt:
        print(f"\n✅ Shutdown cancelled by user")


def run_with_monitoring():
    script_name = "main.py"  # Change this to "test.py" if needed
    max_restarts = 10000  # Maximum number of restarts before giving up
    consecutive_failures = 0
    restart_delay = 60  # Seconds to wait before restarting
    crash_delay = 60  # Seconds to wait if script crashes immediately
    
    restart_count = 0
    
    print(f"🚀 Starting monitor for {script_name}")
    print(f"📊 Max restarts: {max_restarts}")
    print(f"⏱️  Restart delay: {restart_delay}s")
    print(f"💥 Crash delay: {crash_delay}s")
    print("-" * 50)
    
    while restart_count < max_restarts and consecutive_failures < 3:
        try:
            print(f"\n🔄 Starting {script_name} (attempt {restart_count + 1}/{max_restarts}, consecutive failures: {consecutive_failures})")
            print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Run the script
            result = subprocess.run([sys.executable, script_name], 
                                  capture_output=False,  # Show output in real-time
                                  text=True)
            
            # If we get here, the script finished normally
            if result.returncode == 0:
                consecutive_failures = 0  # Reset consecutive failures on success
                print(f"\n✅ {script_name} completed successfully!")
                break
            else:
                print(f"\n⚠️ {script_name} exited with code {result.returncode}")
                consecutive_failures += 1  # Increment consecutive failures
                
        except KeyboardInterrupt:
            print(f"\n🛑 Monitor stopped by user")
            break
        except Exception as e:
            print(f"\n❌ Error running {script_name}: {e}")
            consecutive_failures += 1  # Increment consecutive failures
        
        restart_count += 1
        
        if restart_count < max_restarts:
            print(f"\n⏳ Waiting {restart_delay} seconds before restart...")
            time.sleep(restart_delay)
        else:
            print(f"\n💀 Maximum restarts ({max_restarts}) reached. Stopping monitor.")
    
    shutdown_pc()
    print(f"\n🏁 Monitor finished after {restart_count} attempts")
    print(f"🔥 Consecutive failures: {consecutive_failures}")

if __name__ == "__main__":
    run_with_monitoring() 