def return_vowels(text):
    vowels = 'aeiou'
    return [char for char in text[90:97] if char > '_' and char <= 'x' and (char in vowels)]