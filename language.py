import constants


def choose_language():
    language = input("Please choose a language (English, Spanish, French, German): ")
    if language.capitalize() in constants.AVAILABLE_LANGUAGES:
        print(f"You've selected {language} language.")
        return language.capitalize()
    else:
        print(f"We didn't understand you. We will keep English language for you.")
        return "English"
