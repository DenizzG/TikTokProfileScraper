import asyncio
import sqlite3
import time
from TikTokApi import TikTokApi
import requests
import os
import random, asyncio

# ---------- CONFIG ----------
UMBRELLA_KEYWORDS = [
    "fitness", "makeup", "gaming", "crypto", "travel", "youtube", "twitch", "mental health", "fashion", "comedy",
    "education", "business", "investing", "food", "lifestyle", "art", "tech", "relationships",
    "pets", "music", "startup",
]

RELATED_KEYWORDS = {
    "fitness": [
    "fitness", "gym", "workout", "training", "exercise", "bodybuilding", "weightlifting",
    "powerlifting", "calisthenics", "yoga", "pilates", "crossfit", "strength training",
    "fat loss", "weight loss", "muscle gain", "bulking", "cutting", "home workout",
    "core workout", "leg day", "arm workout", "cardio", "stretching", "warmup",
    "personal trainer", "fitspo", "fitfam", "fitnessmotivation", "fitnessjourney",
    "shredded", "aesthetic physique", "men's fitness", "women's fitness", "6 pack abs",
    "booty workout", "glute workout", "swole", "hypertrophy", "lean bulk", "recomp",
    "hiit", "body recomposition", "no equipment workout", "push day", "pull day"
    ],

    "makeup": [
    "makeup", "skincare", "beauty tips", "makeup tutorial", "foundation routine", 
    "eyeshadow tutorial", "lipstick tutorial", "contour tutorial", "blush tutorial",
    "concealer tutorial", "makeup hacks", "makeup haul", "drugstore makeup", 
    "luxury makeup", "eyeliner tips", "mascara tutorial", "brow shaping", 
    "brow lamination", "full face makeup", "natural makeup", "no makeup look", 
    "bridal makeup", "wedding makeup", "party makeup", "makeup artist", "mua", 
    "makeup trends", "makeup dupes", "viral makeup", "tiktok makeup", 
    "asian makeup", "korean skincare", "glowing skin", "glass skin", 
    "skin prep", "acne coverage", "blemish cover", "highlighting", "baking makeup", 
    "color correcting", "under eye concealer", "lip liner", "nude lipstick", 
    "smokey eye", "cut crease", "lash extensions", "false lashes", "setting spray"
],
    "gaming": [
    "gaming", "pc gaming", "console gaming", "mobile gaming", "esports", "twitch gaming", 
    "youtube gaming", "fortnite", "call of duty", "valorant", "league of legends", 
    "dota 2", "minecraft", "roblox", "csgo", "apex legends", "overwatch", 
    "elden ring", "fifa 24", "nba 2k", "rpg gaming", "mmo gaming", "fps gaming", 
    "battle royale", "speedrun", "gamer setup", "gaming chair", "gaming pc build", 
    "graphics card", "gaming monitor", "streaming setup", "headset review", 
    "gaming news", "gaming leaks", "new games 2025", "gameplay highlights", 
    "funny gaming clips", "pro gamer", "streamer life", "competitive gaming", 
    "multiplayer gaming", "coop gaming", "gaming keyboard", "mechanical keyboard", 
    "aim training", "gaming community", "gamer memes", "gaming addiction",

    # Add many more individual game titles:
    "gta 5", "gta 6", "grand theft auto", "red dead redemption 2", "starfield",
    "hogwarts legacy", "the last of us", "spider man 2", "god of war ragnarok",
    "diablo 4", "lost ark", "genshin impact", "honkai star rail", "baldur's gate 3",
    "palworld", "ark survival evolved", "rust", "escape from tarkov", 
    "battlefield 2042", "pubg", "pubg mobile", "mobile legends", 
    "wild rift", "pokemon unite", "pokemon scarlet violet", 
    "zelda tears of the kingdom", "animal crossing", "splatoon 3",
    "smash bros ultimate", "metroid dread", "halo infinite", "destiny 2",
    "sea of thieves", "star citizen", "assassin's creed mirage", 
    "cyberpunk 2077", "witcher 3", "stardew valley", "hades", 
    "terraria", "valheim", "sons of the forest", "phasmaphobia",
    "among us", "fall guys", "dead by daylight", "league of legends wild rift",
    "osu", "beat saber", "vrchat", "pavlov vr", "population one",
    "ark 2", "warzone 2", "mw3 2025", "roblox bedwars", 
    "fortnite creative 2.0", "valorant montage", "rocket league", 
    "paladins", "smite", "hearthstone", "runescape", "old school runescape",
    "maplestory", "tower of fantasy", "summoners war", "clash royale",
    "clash of clans", "brawl stars", "call of duty mobile", "apex mobile",
    "rise of kingdoms", "war thunder", "world of tanks", "world of warships",
    "monster hunter rise", "monster hunter world", "persona 5", 
    "persona 3 reload", "final fantasy 16", "final fantasy 14", "farming simulator",
    "efootball", "wwe 2k24", "madden 24", "f1 24"
    ],
    "crypto": [
    "crypto", "bitcoin", "ethereum", "solana", "dogecoin", "altcoin", "blockchain",
    "web3", "nfts", "defi", "staking", "yield farming", "crypto trading",
    "crypto investing", "crypto analysis", "bitcoin halving", "crypto wallet",
    "cold wallet", "crypto crash", "crypto bullrun", "crypto bear market",
    "metaverse", "crypto ai", "ai crypto", "airdrops", "crypto pump", "crypto dumps",
    "altseason", "shitcoins", "crypto scams", "crypto security", "crypto regulations",
    "crypto influencer", "crypto tiktok", "crypto news", "crypto strategy",
    "crypto millionaire", "crypto lifestyle", "passive income crypto"
    ],
    "travel": [
    "travel", "travel vlog", "travel tips", "cheap travel", "luxury travel", 
    "travel hacks", "budget travel", "solo travel", "couple travel", "family travel", 
    "van life", "digital nomad", "road trip", "airbnb travel", "hotel reviews", 
    "travel influencer", "vacation ideas", "weekend getaways", "backpacking", 
    "europe travel", "asia travel", "africa travel", "usa travel", "canada travel", 
    "south america travel", "australia travel", "new zealand travel", "cruise travel", 
    "adventure travel", "hiking travel", "camping travel", "travel packing", 
    "minimalist packing", "long flight tips", "visa tips", "passport hacks", 
    "cheap flights", "airport tips", "safari travel", "island travel", "beach vacation", 
    "mountain travel", "ski trips", "snowboarding trips", "honeymoon destinations", 
    "luxury resorts", "hidden gems", "secret destinations", "bucket list travel"
    ],
    "youtube": [
    "travel", "travel vlog", "travel tips", "cheap travel", "luxury travel", 
    "travel hacks", "budget travel", "solo travel", "couple travel", "family travel", 
    "van life", "digital nomad", "road trip", "airbnb travel", "hotel reviews", 
    "travel influencer", "vacation ideas", "weekend getaways", "backpacking", 
    "europe travel", "asia travel", "africa travel", "usa travel", "canada travel", 
    "south america travel", "australia travel", "new zealand travel", "cruise travel", 
    "adventure travel", "hiking travel", "camping travel", "travel packing", 
    "minimalist packing", "long flight tips", "visa tips", "passport hacks", 
    "cheap flights", "airport tips", "safari travel", "island travel", "beach vacation", 
    "mountain travel", "ski trips", "snowboarding trips", "honeymoon destinations", 
    "luxury resorts", "hidden gems", "secret destinations", "bucket list travel"
    ],
    "twitch": [
    "twitch gaming", "twitch streaming", "twitch clips", "twitch highlights", 
    "twitch esports", "twitch just chatting", "twitch debates", "twitch reaction", 
    "twitch drama", "twitch bans", "twitch controversy", "twitch viral", 
    "twitch funny", "twitch memes", "twitch streamer life", "twitch affiliate", 
    "twitch partner", "twitch monetization", "twitch growth", "twitch discoverability", 
    "twitch algorithm", "twitch setup", "twitch pc build", "twitch dual pc", 
    "twitch camera setup", "twitch lighting", "twitch mic review", 
    "twitch gaming chair", "twitch headphones", "twitch battle royale", 
    "twitch fortnite", "twitch call of duty", "twitch valorant", 
    "twitch league of legends", "twitch apex legends", "twitch speedrun", 
    "twitch coaching", "twitch finance", "twitch business", "twitch entrepreneur", 
    "twitch passive income", "twitch masculinity", "twitch dating", "twitch redpill", 
    "twitch self improvement", "twitch motivation", "twitch productivity", 
    "twitch relationships", "twitch manosphere"
    ],
    "mental health": [
    "mental health", "therapy", "counseling", "life coaching", "mindfulness", 
    "anxiety", "depression", "self care", "self healing", "emotional regulation", 
    "healing trauma", "inner child healing", "mental strength", "stress relief", 
    "panic attacks", "ptsd", "self love", "mental performance", "burnout recovery", 
    "journaling", "gratitude practice", "meditation", "breathing techniques", 
    "coping skills", "positive psychology", "cbt therapy", "dbt therapy", 
    "attachment styles", "boundaries", "emotional intelligence", 
    "psychology tips", "relationship anxiety", "social anxiety", 
    "mental health coach", "mental health influencer", "healing journey", 
    "emotional trauma", "reparenting", "healing depression", "anxiety hacks", 
    "overthinking", "imposter syndrome", "high functioning anxiety", 
    "mental clarity", "trauma therapy", "healing mindset", "emotional resilience", 
    "therapy tiktok", "mental health tiktok"
    ],
    "fashion": [
    "fashion", "streetwear", "luxury fashion", "thrifting", "vintage fashion", 
    "clothing haul", "outfit inspiration", "daily outfits", "outfit ideas", 
    "styling tips", "personal styling", "capsule wardrobe", "runway fashion", 
    "modeling", "editorial fashion", "fashion influencer", "fashion trends", 
    "fall fashion", "summer fashion", "winter fashion", "spring fashion", 
    "sustainable fashion", "ethical fashion", "minimalist fashion", "high fashion", 
    "couture", "menswear", "womenswear", "unisex fashion", "plus size fashion", 
    "petite fashion", "fashion accessories", "jewelry trends", "bags trends", 
    "shoes trends", "luxury bags", "hypebeast", "fashion nova", "zara haul", 
    "hm haul", "asos haul", "outfit of the day", "ootd", "wardrobe essentials", 
    "color theory fashion", "fashion week", "paris fashion", "korean fashion", 
    "asian fashion", "streetstyle", "tiktok fashion"
    ],
    "comedy": [
    "comedy", "funny", "pranks", "funny skits", "viral comedy", "funny reactions", 
    "roasts", "standup comedy", "tiktok humor", "tiktok memes", "satire", 
    "dark humor", "relationship jokes", "situational comedy", "observational humor", 
    "funny fails", "reaction videos", "comedy sketches", "impressions", 
    "voice impressions", "funny commentary", "parody videos", "spoof videos", 
    "prank calls", "trolling", "comedic rants", "funny arguments", 
    "couples comedy", "family comedy", "dad jokes", "funny pets", 
    "awkward moments", "office humor", "school humor", "teacher humor", 
    "student humor", "funny stories", "comedic timing", "funny debates", 
    "comedy podcast", "funny podcasts", "internet humor", "funny trends", 
    "funny viral tiktok", "standup clips", "comedic roasting", "viral laughter"
    ],
    "education": [
    "comedy", "funny", "pranks", "funny skits", "viral comedy", "funny reactions", 
    "roasts", "standup comedy", "tiktok humor", "tiktok memes", "satire", 
    "dark humor", "relationship jokes", "situational comedy", "observational humor", 
    "funny fails", "reaction videos", "comedy sketches", "impressions", 
    "voice impressions", "funny commentary", "parody videos", "spoof videos", 
    "prank calls", "trolling", "comedic rants", "funny arguments", 
    "couples comedy", "family comedy", "dad jokes", "funny pets", 
    "awkward moments", "office humor", "school humor", "teacher humor", 
    "student humor", "funny stories", "comedic timing", "funny debates", 
    "comedy podcast", "funny podcasts", "internet humor", "funny trends", 
    "funny viral tiktok", "standup clips", "comedic roasting", "viral laughter"
    ],
    "business": [
    "education", "study tips", "study motivation", "study hacks", "note taking", 
    "productive studying", "pomodoro technique", "student life", "college tips", 
    "high school tips", "exam preparation", "test anxiety", "school hacks", 
    "homework help", "revision tips", "language learning", "learn english", 
    "spanish learning", "french learning", "math help", "science help", 
    "physics tutorial", "chemistry help", "biology help", "economics tutorial", 
    "finance education", "personal development", "self improvement", "public speaking", 
    "career tips", "resume tips", "job interview tips", "time management", 
    "online learning", "distance learning", "productive student", "medical school", 
    "law school", "pharmacy school", "mba tips", "phd life", "educational psychology", 
    "critical thinking", "debate tips", "speed reading", "memory hacks", 
    "learning disability tips", "adhd study tips", "college admissions", "college scholarships"
    ],
    "investing": [
    "investing", "personal finance", "stock market", "real estate investing", 
    "crypto investing", "bitcoin investing", "retirement planning", "passive income", 
    "dividend investing", "index funds", "mutual funds", "etfs", "growth stocks", 
    "value investing", "portfolio management", "financial independence", 
    "fire movement", "401k tips", "roth ira", "compound interest", 
    "day trading", "swing trading", "forex trading", "commodities trading", 
    "risk management", "market cycles", "asset allocation", "economic indicators", 
    "inflation hedge", "interest rates", "wealth building", "high yield savings", 
    "budgeting tips", "money saving hacks", "debt free journey", "credit score tips", 
    "tax strategies", "financial literacy", "investment property", "real estate flipping", 
    "house hacking", "dividend reinvestment", "side hustle income", 
    "millionaire investing habits", "generational wealth", "money management", 
    "stock options trading", "fintech investing", "hedge fund strategies"
    ],
    "food": [
    "food", "cooking", "baking", "meal prep", "meal planning", "healthy recipes", 
    "high protein meals", "vegan recipes", "vegetarian recipes", "paleo recipes", 
    "keto recipes", "gluten free recipes", "street food", "restaurant reviews", 
    "michelin star restaurants", "home cooking", "quick recipes", 
    "one pan recipes", "easy dinner ideas", "air fryer recipes", 
    "slow cooker recipes", "instant pot recipes", "grilling recipes", 
    "bbq recipes", "smoking meats", "dessert recipes", "cake decorating", 
    "pastry recipes", "bread baking", "pizza recipes", "pasta recipes", 
    "international cuisine", "asian recipes", "indian recipes", "mexican food", 
    "italian food", "french food", "japanese food", "sushi recipes", 
    "food hacks", "budget meals", "fine dining", "cooking classes", 
    "plating presentation", "food photography", "food vlogging", "tiktok recipes", 
    "viral food trends", "unique food pairings"
    ],
    "lifestyle": [
    "lifestyle", "daily routine", "morning routine", "night routine", 
    "minimalism lifestyle", "self care routine", "cleaning routine", 
    "home organization", "home decor", "interior design", "productivity routine", 
    "wellness lifestyle", "balance lifestyle", "personal growth", 
    "self improvement", "hygge lifestyle", "aesthetic lifestyle", 
    "vlog lifestyle", "lifestyle influencer", "fashion lifestyle", 
    "beauty lifestyle", "travel lifestyle", "mom lifestyle", 
    "family lifestyle", "home office setup", "remote work life", 
    "digital nomad life", "financial freedom lifestyle", "frugal living", 
    "luxury lifestyle", "manifestation lifestyle", "law of attraction", 
    "goal setting", "vision board", "journaling routine", "mindful living", 
    "decluttering tips", "bucket list ideas", "life hacks", 
    "positive mindset", "daily affirmations", "relationship goals", 
    "fitness lifestyle", "sustainable living", "zero waste living", 
    "off grid living", "tiny house lifestyle", "van life"
    ],
    "art": [
    "art", "drawing", "digital art", "painting", "watercolor art", 
    "oil painting", "acrylic painting", "sketching", "charcoal drawing", 
    "pencil sketch", "portrait art", "anime art", "manga art", "illustration", 
    "graphic design", "logo design", "branding design", "poster design", 
    "tshirt design", "tattoo art", "graffiti art", "street art", "sculpture", 
    "ceramics", "pottery", "printmaking", "screen printing", "fine art", 
    "art school tips", "art commissions", "art portfolio", "art tutorials", 
    "art challenges", "inktober", "procreate art", "adobe illustrator", 
    "adobe photoshop", "adobe fresco", "animation art", "motion graphics", 
    "storyboarding", "3d modeling", "blender art", "vr art", "ai art", 
    "ai generated art", "art business", "selling art online", "art gallery"
    ],
    "tech": [
    "tech", "technology news", "gadget reviews", "iphone tips", "android tips", 
    "laptop reviews", "pc builds", "gaming pc builds", "graphics cards", 
    "tech unboxing", "headphones review", "tech gear", "streaming gear", 
    "productivity tech", "home automation", "smart home devices", 
    "wearable tech", "smartwatch reviews", "tech accessories", 
    "wireless earbuds", "ai technology", "chatgpt", "machine learning", 
    "artificial intelligence", "blockchain technology", "cybersecurity", 
    "web3", "cloud computing", "programming tips", "coding tutorials", 
    "python coding", "javascript coding", "software engineering", 
    "app development", "mobile app development", "saas business", 
    "startup tech", "fintech", "edtech", "healthtech", "robotics", 
    "drone technology", "electric vehicles", "tesla technology", 
    "space tech", "nasa tech", "future technology", "quantum computing", 
    "metaverse technology", "vr ar tech"
    ],
    "relationships": [
    "relationships", "dating advice", "relationship advice", "marriage advice", 
    "breakup advice", "getting over a breakup", "long distance relationship", 
    "relationship goals", "healthy relationships", "toxic relationships", 
    "narcissist recovery", "codependency recovery", "attachment styles", 
    "love languages", "relationship counseling", "couples therapy", 
    "relationship coaching", "relationship red flags", "trust issues", 
    "jealousy in relationships", "communication skills", "emotional intimacy", 
    "dating apps", "tinder advice", "bumble dating tips", "hinge dating tips", 
    "online dating advice", "first date tips", "dating mistakes", "how to flirt", 
    "masculine energy", "feminine energy", "men's dating advice", 
    "women's dating advice", "dating in 2025", "alpha male advice", 
    "relationship psychology", "relationship boundaries", "healing after breakup", 
    "relationship struggles", "relationship therapist", "dating mindset", 
    "high value woman", "high value man", "feminine soft life", 
    "self love before dating", "relationship growth", "attracting healthy partners", 
    "commitment issues"
    ],
    "pets": [
    "pets", "dog training", "puppy training", "dog behavior tips", 
    "puppy behavior problems", "dog grooming", "pet grooming", "cat care", 
    "kitten care", "pet adoption", "animal rescue", "shelter animals", 
    "dog rescue", "cat rescue", "pet parenting", "pet care tips", 
    "dog breeds", "cat breeds", "exotic pets", "parrot care", 
    "reptile care", "hamster care", "guinea pig care", "bunny care", 
    "fish tank setup", "aquarium tips", "pet nutrition", "dog food reviews", 
    "cat food reviews", "pet health", "pet insurance", "pet medication", 
    "vet visits", "senior pet care", "dog walking", "pet sitter tips", 
    "crate training", "leash training", "dog anxiety tips", "cat behavior problems", 
    "dog tricks", "funny pet videos", "pet viral videos", "animal tiktok", 
    "cute pet videos", "pet fails", "dog memes", "cat memes", "funny animal content"
    ],
    "music": [
    "music", "singing tips", "vocal lessons", "music covers", "songwriting", 
    "guitar lessons", "piano lessons", "music producer", "music production", 
    "recording studio", "home studio setup", "microphone reviews", "audio interface", 
    "dj tutorials", "edm production", "rap freestyles", "hip hop beats", 
    "trap beats", "pop music", "rock music", "indie music", "jazz music", 
    "classical music", "instrumental music", "acoustic covers", "lofi music", 
    "vocal warmups", "choir singing", "music industry", "spotify playlists", 
    "tiktok music trends", "viral songs", "soundcloud rapper", 
    "unsigned artist", "beat making", "sample packs", "sound design", 
    "music mixing", "audio mastering", "live performance", "concert clips", 
    "festival performances", "guitar solos", "drum solos", "orchestra clips", 
    "choir performances", "open mic nights", "talent show clips", "musician life", 
    "studio sessions", "song breakdowns"
    ],
    "startup": [
    "startup", "startup ideas", "how to start a startup", "startup pitch", 
    "startup funding", "venture capital", "angel investors", "startup accelerator", 
    "bootstrapping", "lean startup", "founder stories", "startup grind", 
    "product market fit", "startup exits", "early stage startup", "startup marketing", 
    "go to market strategy", "startup growth hacking", "user acquisition", 
    "startup product launch", "founder mental health", "startup leadership", 
    "cofounder advice", "team building startup", "startup failures", 
    "startup pivots", "startup burn rate", "pre seed funding", "seed funding", 
    "series a funding", "series b funding", "unicorn startup", "tech startup", 
    "ai startup", "saas startup", "fintech startup", "healthtech startup", 
    "edtech startup", "biotech startup", "climate tech startup", 
    "ecommerce startup", "marketplace startup", "creator economy startup", 
    "web3 startup", "blockchain startup", "decentralized startup", 
    "hardware startup", "mobile app startup", "b2b startup", "b2c startup", 
    "direct to consumer startup", "subscription box startup", "social media startup", 
    "marketing agency startup", "legaltech startup", "insurtech startup", 
    "proptech startup", "cybersecurity startup", "logistics startup", 
    "supply chain startup", "delivery startup", "subscription startup", 
    "crypto startup", "vr startup", "ar startup", "robotics startup", 
    "agritech startup", "space startup", "clean energy startup", 
    "travel startup", "food delivery startup", "mobility startup", 
    "ai tools startup", "automation startup", "nocode startup", 
    "lowcode startup", "bootstrapped startup", "startup SaaS builder", 
    "startup culture", "startup ecosystem", "startup failures", "founder tips", 
    "solopreneur startup", "indie hacker startup"
    ]

}

# Config
ADDRESS = "p.webshare.io"
PORT = 80
USERNAME = "mvsvqjtt-rotate"
PASSWORD = "3hiao7ruwcug"
ROTATINGPROXY = {"server": f"http://{USERNAME}:{PASSWORD}@{ADDRESS}:{PORT}"}

FETCH_LIMIT = 15
RESET_AFTER = 1  # <-- Number of keywords after which to recreate TikTokApi()
DB_FILE = "tiktok_profiles.db"

os.makedirs("db", exist_ok=True)

# Main async function
async def scrape_profiles():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    seen_usernames = set()
    keyword_counter = 0
    total_keywords = 0

    for umbrella in UMBRELLA_KEYWORDS:
        table_name = umbrella.replace(' ', '_').lower()

        cur.execute(f'''
            CREATE TABLE IF NOT EXISTS "{table_name}" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                nickname TEXT,
                bio TEXT,
                region TEXT,
                verified BOOLEAN,
                followers INTEGER,
                likes INTEGER,
                videos INTEGER,
                keyword TEXT
            )
        ''')
        conn.commit()

        related_keywords = RELATED_KEYWORDS.get(umbrella, [umbrella])
        print(f"\n🔍 Searching for users for umbrella: {umbrella}")

        for keyword in related_keywords:
            keyword_counter += 1
            total_keywords += 1

            # Recreate TikTokApi session every N keywords
            if keyword_counter % RESET_AFTER == 1:
                if keyword_counter > 1:
                    await api.close_sessions()
                    print("🔄 Reinitializing TikTokApi session...")
                api = TikTokApi()
                await api.create_sessions(num_sessions=2, headless=False, proxies=[ROTATINGPROXY], browser="chromium")

            print(f"   ➡️ Using related keyword: {keyword}")
            async for user in api.search.users(search_term=keyword, count=FETCH_LIMIT):
                username = user.username

                if username in seen_usernames:
                    print(f"🔁 Skipping recurring user: {username}")
                    continue

                try:
                    user_data = await api.user(username=username).info()
                    user_info = user_data.get('userInfo', {}).get('user', {})
                    stats = user_data.get('userInfo', {}).get('stats', {})

                    if not user_info or not stats:
                        print(f"⚠️ Empty data for user {username}. Skipping...")
                        continue

                    username = user_info.get('uniqueId', None)
                    if not username:
                        print(f"⚠️ No username found — skipping user.")
                        continue

                    if username in seen_usernames:
                        print(f"🔁 Skipping recurring user after uniqueId: {username}")
                        continue

                    nickname = user_info.get('nickname', '')
                    bio = user_info.get('signature', '')
                    region = user_info.get('region', 'Unknown')
                    verified = user_info.get('verified', False)
                    followers = stats.get('followerCount', 0)
                    likes = stats.get('heartCount', 0)
                    videos = stats.get('videoCount', 0)

                    print(f"👤 {username} ({nickname}) - {followers} followers, {likes} likes, {videos} videos")

                    if followers >= 10000:
                        try:
                            cur.execute(f'''
                                INSERT OR IGNORE INTO "{table_name}"
                                (username, nickname, bio, region, verified, followers, likes, videos, keyword)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (username, nickname, bio, region, int(verified), followers, likes, videos, keyword))
                            print(f"✅ Saved: {username} ({followers} followers)")
                            seen_usernames.add(username)
                        except sqlite3.Error as e:
                            print(f"❌ DB error for {username}: {e}")
                    else:
                        print(f"⏩ Skipped: {username} ({followers} followers)")
                        seen_usernames.add(username)

                except Exception as e:
                    print(f"❌ Unexpected error while processing user {username}: {e}")

            conn.commit()
            if keyword_counter % 2 == 0:
                await asyncio.sleep(random.uniform(0.4, 0.8))
            if keyword_counter % 2 == 1:
                await asyncio.sleep(random.uniform(2, 3.5))

            # 🔧 RANDOM LONGER BREAK every 20 keywords to avoid soft bans
            if total_keywords % 20 == 0:
                print("☕ Taking a longer break...")
                await asyncio.sleep(random.uniform(30, 60))

        print(f"\n✅ Done! All data saved to table '{table_name}'")
        
        #random pause after each umbrella keyword
        await asyncio.sleep(random.uniform(20, 40))

    conn.close()
    try:
        await api.close_sessions()
    except:
        pass

if __name__ == "__main__":
    asyncio.run(scrape_profiles())
