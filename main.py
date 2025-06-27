import asyncio
import sqlite3
import time
from TikTokApi import TikTokApi
import requests
import os
import random, asyncio
import json

"""
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
    "crypto", "bitcoin", "btc", "ethereum", "eth", "solana", "sol", "dogecoin", "doge", "shiba inu", "shib", 
    "altcoin", "altcoins", "blockchain", "web3", "web 3.0", "nfts", "nft art", "crypto nft", 
    "defi", "yield farming", "liquidity mining", "staking", "crypto staking", "crypto farming", 
    "crypto trading", "crypto investing", "crypto analysis", "technical analysis crypto", 
    "bitcoin halving", "crypto wallet", "hardware wallet", "cold wallet", "ledger nano", 
    "crypto crash", "crypto dip", "crypto bullrun", "bull run 2025", "crypto bear market", 
    "crypto winter", "metaverse", "crypto metaverse", "crypto ai", "ai crypto", "airdrops", 
    "crypto pump", "pump and dump", "crypto dumps", "altseason", "shitcoins", "memecoins", 
    "crypto scams", "crypto fraud", "rugpull", "rug pull", "crypto hacks", "crypto security", 
    "crypto regulations", "crypto tax", "crypto fomo", "crypto fud", "crypto whales", 
    "crypto influencers", "crypto tiktok", "crypto twitter", "crypto youtube", 
    "crypto millionaires", "crypto lifestyle", "passive income crypto", "crypto bots", 
    "trading bots", "arbitrage bots", "crypto arbitrage", "leverage trading", "crypto leverage", 
    "liquidation", "margin trading", "derivatives crypto", "crypto futures", 
    "crypto exchanges", "binance", "kraken", "coinbase", "kucoin", "okx", "bybit", "bitget",
    "centralized exchange", "decentralized exchange", "dex", "uniswap", "pancakeswap", 
    "crypto launchpad", "presale crypto", "pre-sale crypto", "IDO", "IEO", "ICO", 
    "tokenomics", "token sale", "crypto portfolio", "portfolio rebalancing", 
    "crypto prediction", "price prediction crypto", "price target bitcoin", 
    "ethereum merge", "bitcoin etf", "spot etf bitcoin", "crypto regulations 2025", 
    "cbdc", "central bank digital currency", "stablecoin", "usdt", "usdc", "tether", 
    "smart contracts", "ethereum smart contracts", "solana smart contracts", 
    "layer 1 crypto", "layer 2 crypto", "optimism", "arbitrum", "polygon", "zk rollup", 
    "zk evm", "crypto mining", "proof of work", "proof of stake", "validator nodes", 
    "crypto governance", "decentralized governance", "crypto DAO", "crypto communities", 
    "crypto discord", "crypto telegram", "crypto signals", "crypto signal group", 
    "copy trading", "trading signals", "scalping crypto", "crypto swing trading", 
    "crypto day trading", "crypto education", "crypto coaching", "learn crypto", 
    "crypto fundamentals", "on-chain analysis", "glassnode", "crypto kyc", 
    "anti-money laundering crypto", "crypto compliance", "crypto lawsuits", 
    "ftx collapse", "sbf trial", "crypto bankruptcy", "crypto audit", 
    "crypto influencer marketing", "crypto sponsorships", "crypto partnerships", 
    "crypto adoption", "crypto mainstream", "crypto mass adoption", "crypto news", 
    "crypto headlines", "breaking crypto", "crypto jobs", "crypto careers", 
    "crypto software developer", "blockchain developer", "web3 jobs", "crypto startup", 
    "venture capital crypto", "crypto hedge fund", "crypto market cap", 
    "bitcoin dominance", "bitcoin maximalist", "ethereum vs solana", 
    "crypto flipping", "crypto nodes", "passive income nodes", "crypto passive income 2025", 
    "crypto retirement", "crypto long term investing", "crypto generational wealth", 
    "crypto freedom", "bitcoin price forecast", "crypto documentaries", "crypto scams exposed"
    ],
"""


# ---------- CONFIG ----------
UMBRELLA_KEYWORDS = [
    "startup", "lifestyle", "mental health", "business","youtube", "twitch", "comedy",
    "education", "investing", "food",  "art", "tech", "relationships",
    "pets", "personal_trainer", "strength_training", "yoga", "running"
]

RELATED_KEYWORDS = {
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
    "solopreneur startup", "indie hacker startup", "startup investor pitch", 
    "incubator startup", "startup weekend", "demo day startup", 
    "minimum viable product", "founder productivity", "startup mentorship", 
    "startup business model", "go to market plan", "scaling a startup", 
    "startup sales strategy", "startup community", "early traction", 
    "startup investor deck", "startup legal advice", "founder equity", 
    "startup hiring", "equity vs salary", "startup story", 
    "startup reality", "startup hustle", "bootstrap journey", 
    "founder mindset", "startup partnerships", "founder execution", 
    "idea validation", "startup roadmap", "pitch deck tips", 
    "investor relations", "startup networking", "startup tips", 
    "founder grind", "startup fundraising journey"
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
    "off grid living", "tiny house lifestyle", "van life",
    "aesthetic morning", "healthy lifestyle", "reset day", 
    "simple living", "intentional living", "slow living", 
    "routine vlog", "evening routine", "clean girl aesthetic", 
    "cozy lifestyle", "soft life", "elegant lifestyle", 
    "realistic routine", "lifestyle vlog", "declutter routine", 
    "wellness routine", "home life", "morning vlog", 
    "glow up routine", "that girl lifestyle", "organized living", 
    "clean house aesthetic", "day in the life", "cozy routine", 
    "minimalist routine", "calm living", "daily habits", 
    "morning habits", "evening habits", "self discipline routine", 
    "comfort living", "peaceful lifestyle", "serene aesthetic"
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
    "learning disability tips", "adhd study tips", "college admissions", "college scholarships",
    "entrepreneurship", "startup advice", "side hustle", "business ideas", 
    "online business", "small business tips", "freelance tips", "ecommerce business", 
    "dropshipping guide", "social media marketing", "content strategy", 
    "business planning", "business mindset", "sales strategy", 
    "business growth", "startup growth", "branding tips", "digital marketing tips", 
    "passive income ideas", "financial planning", "investment basics", 
    "business funding", "bootstrapping", "marketing funnel", 
    "customer acquisition", "client outreach", "pitch deck tips", 
    "linkedin growth", "remote work tips", "business travel", 
    "professional networking", "time blocking", "workflow management", 
    "solopreneur life", "business podcast", "email marketing strategy"
    ],

    "youtube": [
    "travel", "travel vlog", "travel blogger", "travel content creator", "travel reels", 
    "travel tips", "cheap travel", "luxury travel", "travel hacks", "travel hacks 2025", 
    "budget travel", "solo travel", "solo female travel", "couple travel", 
    "family travel", "van life", "van life europe", "digital nomad", "remote work travel", 
    "travel vloggers", "travel documentary", "road trip", "airbnb travel", 
    "hotel reviews", "hostel reviews", "motel hacks", "luxury resorts", "eco hotels", 
    "glamping", "camping hacks", "camping gear", "camping vlogs", "backpacking", 
    "backpacking southeast asia", "backpacking south america", "gap year travel", 
    "weekend getaways", "vacation ideas", "hidden gems travel", "underrated destinations", 
    "bucket list travel", "dream destinations", "off the beaten path", 
    "sustainable travel", "eco friendly travel", "green travel", "digital nomad visa", 
    "visa tips", "passport hacks", "visa free countries", "passport ranking", 
    "travel safety", "travel insurance", "cheap flights", "flight hacks", 
    "airfare deals", "airport hacks", "airport lounge reviews", "priority pass", 
    "lounge access hacks", "long haul flights", "jet lag hacks", "travel packing", 
    "packing cubes", "minimalist packing", "ultralight packing", "travel gear review", 
    "camera gear for travel", "drone travel videos", "dji travel", "gopro travel", 
    "travel vlogging gear", "editing travel vlogs", "travel monetization", 
    "youtube travel monetization", "travel affiliate marketing", "safari travel", 
    "wildlife travel", "antarctica cruise", "alaska cruise", "cruise hacks", 
    "cruise vlog", "luxury cruises", "adventure travel", "hiking travel", 
    "mountain travel", "alps hiking", "patagonia travel", "peru travel", 
    "machu picchu travel", "safari lodge", "luxury safari", "desert travel", 
    "oasis travel", "island hopping", "beach vacation", "honeymoon travel", 
    "romantic getaways", "spa resorts", "hot springs travel", "ski trips", 
    "snowboarding trips", "polar travel", "aurora borealis travel", "northern lights travel", 
    "train travel", "luxury train travel", "orient express", "japan travel", 
    "tokyo travel", "kyoto travel", "bali travel", "indonesia travel", "thailand travel", 
    "europe travel", "italy travel", "paris travel", "london travel", "usa travel", 
    "new york travel", "california travel", "hawaii travel", "canada travel", 
    "australia travel", "new zealand travel", "africa travel", "morocco travel", 
    "egypt travel", "south africa travel", "south america travel", 
    "brazil travel", "argentina travel", "chile travel"
    ],
    "twitch": [
    "twitch", "twitch streaming", "twitch streamer", "twitch creator", "twitch partner", 
    "twitch affiliate", "twitch clips", "twitch highlights", "twitch gaming", 
    "twitch esports", "twitch tournaments", "twitch speedrun", "twitch charity stream", 
    "twitch coaching", "twitch pro players", "twitch reaction", "twitch just chatting", 
    "twitch talk show", "twitch debates", "twitch interviews", "twitch hot tub meta", 
    "twitch asmr", "twitch music stream", "twitch karaoke", "twitch concerts", 
    "twitch creative", "twitch art", "twitch coding", "twitch study stream", 
    "twitch finance", "twitch investing", "twitch self improvement", "twitch entrepreneur", 
    "twitch business", "twitch startup", "twitch motivation", "twitch redpill", 
    "twitch manosphere", "twitch relationships", "twitch dating", "twitch mental health", 
    "twitch therapy", "twitch burnout", "twitch motivation stream", "twitch schedule", 
    "twitch passive income", "twitch monetization", "twitch income report", 
    "twitch discoverability", "twitch growth tips", "twitch growth 2025", 
    "twitch algorithm", "twitch seo", "twitch networking", "twitch collaboration", 
    "twitch raids", "twitch hosting", "twitch stream sniping", "twitch mods", 
    "twitch mod drama", "twitch bans", "twitch appeals", "twitch tos", 
    "twitch copyright", "twitch dmca", "twitch drama", "twitch viral", 
    "twitch controversies", "twitch politics", "twitch cancel culture", 
    "twitch harassment", "twitch fanbase", "twitch simps", "twitch subs", 
    "twitch subathon", "twitch prime", "twitch revenue split", "twitch pay cut", 
    "twitch vs kick", "kick streaming", "kick drama", "kick gambling", 
    "kick vs twitch", "youtube streaming", "twitch alternative", "rumble streaming", 
    "twitch setup", "twitch pc build", "streaming pc", "dual pc streaming", 
    "streamlabs obs", "twitch obs", "twitch overlays", "twitch camera setup", 
    "twitch lighting", "twitch mic setup", "twitch audio issues", "twitch green screen", 
    "twitch vtuber", "vtuber debut", "vtuber drama", "twitch cosplay", 
    "twitch IRL", "irl streamers", "travel stream", "twitch food streams", 
    "twitch fitness", "twitch workout stream", "twitch cooking stream", 
    "twitch pets", "twitch funny moments", "twitch fails", "twitch memes", 
    "twitch influencers", "twitch famous streamers", "twitch viral clips", 
    "twitch sponsorships", "twitch ad revenue", "twitch brand deals"
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

    "personal_trainer": [
    "personal trainer", "fitness coach", "online personal trainer", "gym trainer",
    "personal training tips", "personal trainer advice", "certified personal trainer",
    "personal trainer journey", "how to become a personal trainer", "pt course",
    "personal trainer certification", "personal trainer transformation",
    "personal trainer day in the life", "personal trainer vlog", "fitness trainer",
    "personal trainer motivation", "client transformation", "training clients",
    "training programs", "pt pricing", "online coaching", "hybrid coaching model",
    "personal training business", "fitness coaching business", "how to get pt clients",
    "personal trainer branding", "fitness content ideas", "gym marketing",
    "fitness coaching niche", "beginner workout clients", "client retention tips",
    "in person vs online coaching", "how to scale personal training", 
    "lead generation for personal trainers", "personal trainer niche ideas",
    "group training", "bootcamp coaching", "high ticket fitness coaching",
    "weight loss clients", "muscle building clients", "postpartum fitness clients",
    "sports performance coach", "athletic training", "nutrition coach",
    "strength training clients", "mobility coaching", "hypertrophy training",
    "powerlifting coach", "bodybuilding coach", "functional fitness trainer",
    "crossfit coach", "HIIT trainer", "trx training", "calisthenics trainer",
    "personal trainer reels", "fitness tiktok ideas", "fitness coaching app",
    "workout programming", "custom workout plans", "training plan template",
    "training split", "training plan results", "exercise demo videos",
    "pt social proof", "client before and after", "gym content ideas",
    "gym trainer tips", "pt mindset", "personal trainer mistakes",
    "fitness coach lessons", "coaching transformation stories",
    "build a personal training brand", "scaling pt income", 
    "personal trainer online course", "monthly coaching program",
    "weekly check-ins fitness", "fitness accountability coaching",
    "mindset coach fitness", "online fitness business", "personal trainer community",
    "fitness lead magnets", "high ticket coaching offer", "coaching DMs",
    "fitness sales call script", "pt sales funnel", "gym funnel", 
    "personal trainer scheduling app", "calorie tracking for clients",
    "macro coach", "client workout tracking", "coaching results dashboard",
    "pt check-in systems", "online coaching tools", "build coaching systems"
],
"strength_training": [
    "strength training", "powerlifting", "bodybuilding", "weightlifting", 
    "olympic lifting", "hypertrophy training", "muscle building", "strength coach",
    "online strength coach", "lifting program", "custom training plan", 
    "beginner lifting program", "powerlifting program", "bodybuilding split",
    "push pull legs", "upper lower split", "training periodization",
    "progressive overload", "compound lifts", "accessory work",
    "squat bench deadlift", "bench press form", "deadlift setup", 
    "how to squat properly", "barbell back squat", "sumo deadlift vs conventional",
    "lifting form check", "lifting transformation", "powerbuilding", 
    "cutting vs bulking", "dirty bulk vs clean bulk", "how to bulk properly",
    "lean muscle mass", "recomping", "natural bodybuilding", 
    "steroid-free bodybuilding", "natty or not", "body recomposition", 
    "posing tips bodybuilding", "bodybuilding prep", "competition prep", 
    "peak week bodybuilding", "stage lean", "posing coach", 
    "bodybuilder diet", "meal prep bodybuilding", "eating to grow muscle",
    "macros for bulking", "strength vs hypertrophy", "powerlifting meet prep", 
    "peaking for powerlifting", "weight class strategy", 
    "lifting for women", "female powerlifter", "female bodybuilder", 
    "bodyweight strength training", "barbell lifting", "dumbbell workout plan",
    "lifting motivation", "gym lifting clips", "powerlifting TikTok", 
    "bodybuilding TikTok", "strength coaching tips", "online lifting program",
    "home gym lifting", "lifting accessories", "lifting belt guide", 
    "knee sleeves vs wraps", "lifting shoes", "deadlift socks", 
    "recovery for lifters", "sleep and muscle growth", "how to avoid burnout",
    "lifting injuries", "lifting with bad knees", "shoulder pain bench press",
    "lifting warmup", "mobility for lifters", "strength gains plateau", 
    "deload week", "lifting mindset", "gym anxiety lifting", 
    "first powerlifting meet", "how to enter bodybuilding show", 
    "lifter transformation story", "from skinny to strong", "natty gains", 
    "powerlifting vs bodybuilding", "training to failure", 
    "volume vs intensity", "RPE scale", "RIR explained", 
    "one rep max tips", "lifting PR", "how to test your max",
    "coach reacts to lifter", "lifter critique", "bar path analysis",
    "strength TikTok", "gym lifting reel", "lifting journey", 
    "intermediate lifting tips", "advanced hypertrophy", 
    "lifting program review", "powerlifting accessories", "deadlift tutorial",
    "bench tutorial", "squat depth check", "lifter content ideas"
],
"yoga": [
    "yoga", "yoga practice", "daily yoga", "morning yoga", "evening yoga", 
    "yoga for beginners", "yoga for flexibility", "yoga for strength", 
    "yoga for anxiety", "yoga for stress relief", "yoga for back pain", 
    "yoga for hips", "yoga for core", "yoga for runners", "yoga for athletes", 
    "power yoga", "vinyasa yoga", "hatha yoga", "yin yoga", "restorative yoga", 
    "ashtanga yoga", "kundalini yoga", "hot yoga", "yoga nidra", 
    "prenatal yoga", "postnatal yoga", "yoga for kids", "chair yoga", 
    "yoga for seniors", "beginner yoga flow", "intermediate yoga flow", 
    "advanced yoga flow", "yoga flow for mobility", "yoga for balance", 
    "yoga for posture", "yoga for energy", "yoga for better sleep", 
    "sun salutation tutorial", "chaturanga tips", "yoga alignment tips", 
    "yoga pose breakdown", "yoga pose names", "yoga pose progression", 
    "headstand tutorial", "handstand prep", "crow pose guide", 
    "wheel pose tutorial", "splits flexibility yoga", 
    "yoga flexibility journey", "daily yoga challenge", 
    "30 day yoga challenge", "yoga mat review", "yoga gear must haves", 
    "yoga block exercises", "yoga strap stretches", "yoga at home", 
    "yoga in the park", "sunrise yoga", "yoga lifestyle", "yogi mindset", 
    "how to become a yoga teacher", "yoga teacher training", 
    "online yoga teacher training", "yoga certification", 
    "yoga teacher life", "teaching yoga online", "yoga class planning", 
    "sequencing a yoga class", "mindful movement", "yoga and meditation", 
    "yoga breathwork", "pranayama basics", "breath awareness practice", 
    "yoga and journaling", "self care with yoga", "yoga for self love", 
    "affirmations and yoga", "spiritual yoga practice", 
    "yoga community", "yoga retreat", "yoga travel", 
    "yoga transformation", "yoga before and after", "yoga motivation", 
    "flexibility progress", "yoga tutorial", "yoga correction video", 
    "yoga reel ideas", "yoga TikTok trends", "yoga duet reaction", 
    "yoga fail analysis", "yoga for every body", "inclusive yoga", 
    "plus size yoga", "accessible yoga", "yoga modifications", 
    "yoga for injury recovery", "yoga for neck pain", "shoulder opening yoga", 
    "hip opening sequence", "yoga for menstrual cramps", 
    "yoga for digestion", "gentle yoga routine", "quick yoga flow", 
    "5 minute yoga", "10 minute yoga", "yoga mobility routine", 
    "yoga for beginners at home", "yoga for relaxation", 
    "meditative yoga flow", "yoga inspiration", "yoga content ideas"
],
"running": [
    "running", "running tips", "how to start running", "beginner running plan", 
    "5k training plan", "10k training plan", "half marathon training", 
    "marathon training plan", "couch to 5k", "couch to 10k", 
    "running for beginners", "running form tips", "how to run properly", 
    "improve running speed", "running cadence explained", "foot strike running", 
    "breathing while running", "running posture", "common running mistakes", 
    "running gear essentials", "best running shoes", "running shoe review", 
    "how to choose running shoes", "carbon plate shoes", 
    "daily trainer vs race day shoes", "running shoe rotation", 
    "running apparel", "running watch comparison", "garmin running watch", 
    "strava running tips", "running motivation", "running vlog", 
    "running transformation", "runner before and after", "runner body changes", 
    "running weight loss", "fat burning runs", "zone 2 running", 
    "heart rate training", "VO2 max training", "long slow distance runs", 
    "tempo runs explained", "interval running workout", 
    "fartlek workout running", "hill sprints running", 
    "treadmill running tips", "indoor running drills", "running drills", 
    "dynamic warm up for runners", "post run stretches", "runner mobility", 
    "injury prevention running", "shin splints help", "IT band pain running", 
    "runner’s knee fix", "plantar fasciitis running", 
    "recovery after long run", "running and sleep", 
    "running while fasting", "running and hydration", 
    "running fuel for long runs", "running gel timing", "electrolytes running", 
    "how to pace your run", "race day prep", "marathon day vlog", 
    "running checklist", "running in the heat", "running in the cold", 
    "rainy day running tips", "night running safety", "running mindset", 
    "mental toughness running", "runner’s high", 
    "daily running challenge", "30 day running challenge", 
    "run streak journey", "strava art", "running with a dog", 
    "running with a stroller", "trail running basics", 
    "ultramarathon training", "trail shoes vs road shoes", 
    "hydration vest running", "race recap vlog", "runner TikTok", 
    "running content ideas", "running aesthetic", "track running", 
    "track workouts explained", "sprinter vs distance runner", 
    "cross country running", "athlete running form", "how to run faster", 
    "run club", "online run coaching", "running coach tips", 
    "virtual running plan", "custom running plan", "run training app", 
    "running performance metrics", "best running playlist", 
    "running with friends", "fun run ideas"
]




}

# Config
ADDRESS = "us.decodo.com"
PORT = 10000
USERNAME = "denuser"
PASSWORD = "E6~Xjtrfqy76Qa4eVz"

#ROTATINGPROXY = {"server": f"socks5h://TikTokApi:0H3B4g9ydo_BgKwbsr@gate.decodo.com:7000"}
ROTATINGPROXY = [{
    "server": "http://us.decodo.com:10000",
    "username": "denuser",
    "password": "E6~Xjtrfqy76Qa4eVz"
    }]

#ROTATINGPROXY = {"server": f"http://{USERNAME}:{PASSWORD}@{ADDRESS}:{PORT}"}

FETCH_LIMIT = 15
RESET_AFTER = 2  # <-- Number of keywords after which to recreate TikTokApi()
DB_FILE = "tiktok_profiles.db"

os.makedirs("db", exist_ok=True)

# Config
PROGRESS_FILE = "progress.json"

# Load previous progress
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"umbrella": None, "keyword_index": 0}

# Save progress after each keyword
def save_progress(umbrella, keyword_index):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({"umbrella": umbrella, "keyword_index": keyword_index}, f)

async def scrape_profiles():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    seen_usernames = set()
    keyword_counter = 0
    total_keywords = 0

    progress = load_progress()
    progress_hit = False

    api = TikTokApi()
    await api.create_sessions(num_sessions=1, headless=False, browser="chromium")
    await asyncio.sleep(random.uniform(0.3, 0.6))

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

        # Skip umbrellas we already finished
        if not progress_hit:
            if umbrella != progress["umbrella"] and progress["umbrella"] is not None:
                print(f"⏩ Skipping umbrella: {umbrella}")
                continue
            else:
                progress_hit = True

        for idx, keyword in enumerate(related_keywords):

            # Skip keywords we've already processed
            if umbrella == progress["umbrella"] and idx < progress["keyword_index"]:
                continue

            keyword_counter += 1
            total_keywords += 1

            if keyword_counter % RESET_AFTER == 0:
                await api.close_sessions()
                print("🔄 Reinitializing TikTokApi session...")
                await asyncio.sleep(random.uniform(0.3, 0.6))
                api = TikTokApi()
                await api.create_sessions(num_sessions=1, headless=False, browser="chromium")
                await asyncio.sleep(random.uniform(0.3, 0.6))

            print(f"    ➡️ Using related keyword: {keyword}")

            try:
                async for user in api.search.users(search_term=keyword, count=FETCH_LIMIT):
                    username = user.username
                    await asyncio.sleep(random.uniform(0.2, 0.4))

                    if username in seen_usernames:
                        print(f"🔁 Skipping recurring user: {username}")
                        continue

                    try:
                        user_data = await api.user(username=username).info()
                        await asyncio.sleep(random.uniform(0.2, 0.4))

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
                save_progress(umbrella, idx+1)

            except Exception as e:
                print(f"❌ Error during search: {e}")

            if keyword_counter % 2 == 0:
                await asyncio.sleep(random.uniform(0.4, 0.8))
            if keyword_counter % 2 == 1:
                await asyncio.sleep(random.uniform(2, 3.5))

            if total_keywords % 20 == 0:
                print("☕ Taking a longer break...")
                await asyncio.sleep(random.uniform(15, 45))

        print(f"\n✅ Done! All data saved to table '{table_name}'")
        await asyncio.sleep(random.uniform(15, 30))

    conn.close()
    try:
        await api.close_sessions()
    except:
        pass


if __name__ == "__main__":
    asyncio.run(scrape_profiles())
