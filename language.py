AVAILABLE_LANGUAGES = ["English", "Spanish", "French", "German"]

def choose_language():
    language = input("Please choose a language (English, Spanish, French, German): ")
    if language.capitalize() in AVAILABLE_LANGUAGES:
        return language.capitalize()
    else:
        return "English"



choose_language()
