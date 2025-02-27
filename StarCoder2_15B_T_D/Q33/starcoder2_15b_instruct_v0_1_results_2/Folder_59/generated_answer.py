def return_vowels(text):
    return [char for i, char in enumerate(text) if i >= 8 and i < 9 and (char in 'aeiou') and (char > 'Y') and (char <= 's')]