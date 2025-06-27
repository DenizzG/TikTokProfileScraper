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
