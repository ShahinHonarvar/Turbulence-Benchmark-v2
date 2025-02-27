def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[328:455] if char in vowels and char < 'z']