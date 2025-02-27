def return_vowels(text):
    vowels = 'aeiou'
    return [c for i, c in enumerate(text) if 23 <= i < 85 and c in vowels and (c > 'W') and (c <= 'v')]