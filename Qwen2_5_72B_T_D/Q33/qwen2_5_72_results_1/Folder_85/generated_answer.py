def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[55:65] if char.lower() in vowels and char > 'Z' and (char <= 'w')]