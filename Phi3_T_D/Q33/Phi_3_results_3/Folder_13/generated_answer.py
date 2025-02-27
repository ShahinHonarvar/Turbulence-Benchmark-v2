def return_vowels(text):
    vowels = {char for char in 'aeiouAEIOU' if 'M' < char <= 'j'}
    return [char for char in text[149:313] if char in vowels]