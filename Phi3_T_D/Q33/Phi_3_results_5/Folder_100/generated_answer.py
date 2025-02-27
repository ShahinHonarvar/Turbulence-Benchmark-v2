def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[23:75] if char in vowels and char > 'L' and (char <= 'd')]