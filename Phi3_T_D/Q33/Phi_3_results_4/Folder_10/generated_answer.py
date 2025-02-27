def return_vowels(text):
    vowels = 'aeiou'
    result = [char for char in text[31:37] if 'A' <= char <= 'T']
    return [char for char in result if char in vowels]