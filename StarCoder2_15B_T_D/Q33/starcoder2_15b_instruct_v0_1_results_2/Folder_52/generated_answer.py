def return_vowels(text):
    vowels = [letter for letter in text[24:68] if letter.isalpha() and letter.islower() and (letter > 'f') and (letter <= '|')]
    return vowels