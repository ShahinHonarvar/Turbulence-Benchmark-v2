def return_vowels(text):
    vowels = 'aeiou'
    result = [char for char in text[3:9] if char in vowels and char > 'S' and (char <= 'U')]
    return result