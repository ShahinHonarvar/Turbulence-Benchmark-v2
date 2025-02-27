def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[10:83] if char in vowels and '%' < char <= 'e']