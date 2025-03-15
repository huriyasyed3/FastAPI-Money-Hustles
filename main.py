from fastapi import FastAPI  #  import FastAPI class
import random
from fastapi.responses import RedirectResponse 

app = FastAPI()

# Two GET endpoints:
# 1- side_hustles
# 2- money_quotes

@app.get('/', include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
    
side_hustles = [
    "Freelancing - Start offering your skill online",
    "Graphic Design - Create logos, posters, and visuals for clients",
    "Content Writing - Write blogs, articles, and website content",
    "Affiliate Marketing - Earn commission by promoting products",
    "Online Tutoring - Teach students online in your expertise",
    "Dropshipping - Sell products online without managing inventory",
    "Social Media Management - Handle business social accounts",
    "Virtual Assistance - Help businesses with online tasks",
    "Print on Demand - Sell custom-designed T-shirts and products",
    "Stock Photography - Sell high-quality images online",
    "Video Editing - Edit videos for YouTube, ads, and social media",
    "Voice Over Work - Record voiceovers for videos and podcasts",
    "Handmade Crafts Selling - Sell handmade items on Etsy",
    "Etsy Store - Open an online shop for handmade or digital goods",
    "Blogging - Write and monetize your blog",
    "YouTube Channel - Create videos and earn from ads and sponsorships",
    "Podcasting - Start a podcast and earn from sponsorships",
    "Fitness Coaching - Offer online fitness training and diet plans",
    "App Development - Build and sell mobile applications",
    "Online Course Creation - Teach skills and sell courses online",
    "NFT Selling - Create and sell digital art as NFTs",
    "Crypto Trading - Buy and sell cryptocurrencies for profit",
    "Data Entry - Work on simple data entry tasks online",
    "Transcription Services - Convert audio into written text",
    "UI/UX Design - Design user-friendly apps and websites",
    "Digital Marketing - Help businesses grow online",
    "SEO Consultancy - Optimize websites to rank better on Google",
    "Selling E-books - Write and sell e-books online",
    "Photography - Capture and sell professional photos",
    "Handmade Jewelry Selling - Create and sell jewelry"
]

money_quotes = [
    "Money is a tool. Used properly, it makes something beautiful. Used wrong, it makes a mess. - Bradley Vinson",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "The more you learn, the more you earn. - Warren Buffett",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "It’s not about having a lot of money. It’s about having a lot of options. - Chris Rock",
    "Rich people stay rich by living like they’re broke. Broke people stay broke by living like they’re rich. - Unknown",
    "The key to wealth is learning how to make money work for you. - Robert Kiyosaki",
    "Don’t work for money; make it work for you. - Robert Kiyosaki",
    "The rich invest their money and spend what is left. The poor spend their money and invest what is left. - Unknown",
    "A big part of financial freedom is having your heart and mind free from worry about the what-ifs of life. - Suze Orman",
    "Making money is common sense. It’s not rocket science. But unfortunately, when it comes to money, common sense is uncommon. - Robert Kiyosaki",
    "Your salary is the bribe they give you to forget your dreams. - Unknown",
    "Never depend on a single income. Make investment to create a second source. - Warren Buffett",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "Opportunities come infrequently. When it rains gold, put out the bucket, not the thimble. - Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "Money grows on the tree of persistence. - Japanese Proverb",
    "The goal isn’t more money. The goal is living life on your terms. - Chris Brogan",
    "Too many people spend money they earned to buy things they don’t want to impress people that they don’t like. - Will Rogers"
]

@app.get('/side_hustles')
def get_side_hustles(apikey: str):
    """Return a random side hustle idea"""
    if apikey != "1234567890":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get('/money_quotes')
def get_money_quotes(apikey: str):
    """Return a random money quote"""
    if apikey != "1234567890":
        return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
