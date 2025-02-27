def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[3:9] if char in vowels and char > 'S' and (char <= 'U')]