def return_vowels(text):
    vowels = [char for char in text[529:828] if char.isalpha() and char.lower() in 'aeiou' and (char > 'U') and (char <= 'l')]
    return vowels