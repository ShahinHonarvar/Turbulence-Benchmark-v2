def return_vowels(text):
    vowels_between = [letter for letter in text[4:8] if 'p' < letter <= 'r' and letter.lower() in 'aeiou']
    return vowels_between