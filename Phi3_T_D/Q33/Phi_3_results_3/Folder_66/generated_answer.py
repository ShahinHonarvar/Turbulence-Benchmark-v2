def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[63:79] if char in vowels and char > 'D' and (char <= 'y')]