def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[45:76] if char in vowels and char > 'b' and (char <= 'z')]