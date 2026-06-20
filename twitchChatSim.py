import random, time

#basically a twitch chat simulator, with random usernames, messages

#CREATED BY @DIFFIKULTD44



username_words1 = ["DIFFIKULTD", "shadow", "adaptable", "brave", "creative", "dazzling", "eager", "fearless", "gentle", "happy", "inventive", "joyful", "keen", "lively", "mysterious", "noble", "optimistic", "polished", "quick", "radiant", "sincere", "talented", "unique", "vibrant", "wise", "xenial", "youthful", "zealous", "amiable", "bright", "calm", "determined", "eloquent", "fancy", "graceful", "helpful", "independent", "jovial", "kind", "lucid", "magnificent", "neat", "outstanding", "proud", "quiet", "resilient", "stellar", "thoughtful", "understanding", "vivid", "witty", "zesty"]

username_words2 = ["lord", "apple", "book", "car", "dog", "elephant", "forest", "guitar", "house", "island", "jacket", "kangaroo", "lantern", "mountain", "notebook", "ocean", "pencil", "queen", "river", "sunflower", "table", "umbrella", "village", "window", "xylophone", "yacht", "zebra", "anchor", "balloon", "camera", "diamond", "envelope", "feather", "globe", "horizon", "insect", "journey", "key", "lantern", "mirror", "needle", "oasis", "pirate", "quartz", "rainbow", "telescope", "uniform", "volcano", "whistle", "yarn", "zenith"]



words = ["HUH", "dank", "LMAO", "LOL", "sonion ring", "bruh", "tuff", "dih", "goofy", "ur bald", "big silly", "pog", "mods suck", "rigged", "l streamer", "w", "o7", "o7", "o7", "o7", "o7", "o7", "o7", "o7", "o7", "w", "subbed", "e", "skibidi", "rizz", "L", "fail", "throwing", "clipfarming", "omegaLUL", "are we deadass", "chat is this real", "bro not him", "blud", "w stream", "gg", "poggies", "pog", "I WAS HERE", "I WAS HERE", "yap", "play roblox", "i followed", "tuff", "we are trapped in the basement", "play peggle", "you look like a thumb", "L gameplay"]




def message_generator():
    amount_of_words = random.randint(1, 6)
    # 1. Grab a unique random sample of words from the list
    chosen_words = random.choices(words, k=amount_of_words)
    # 2. Join them with spaces into a single continuous sentence layout
    sentence = " ".join(chosen_words)

    username = (random.choice(username_words1) + random.choice(username_words2))

    # 3. Pick a random number between 31 and 36 for the text color code
    color_code = random.randint(31, 36)

    # 4. Wrap the username in the ANSI escape codes using the random number
    return f"\033[{color_code}m{username}\033[0m: {sentence}"


    

input("press enter to begin chat>>>")

while True:
    message_cooldown = random.uniform(0.4, 5.0)
    time.sleep(message_cooldown)
    message = message_generator()
    print(message)
