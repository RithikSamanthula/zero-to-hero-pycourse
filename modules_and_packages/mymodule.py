import random

global random_num

def inspirational_quotes():
    quotes = ["It always seems impossible until it's done.", "Follow your heart.", "Never let your fear decide your fate.", "Take the risk or loose the chance.","Wisdom beings in wonder.","You are your choices","Think outside the box","Faith can move mountains","Courage doesn't always roar","Success is 99 percent failure","Wake up and live","Let life surprise you", "Live a good story.", "You only live once","Think less live more","Never doubt your instinct","Smile, it's free therapy","Collect moments, not things","Don't give up, ever.","Live long and prosper."]

    random_num = random.randint(0,len(quotes) - 1)

    print(quotes[random_num])

