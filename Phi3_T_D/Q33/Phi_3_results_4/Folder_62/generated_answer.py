def return_vowels(s):
    vowels = 'aeiou'
    target_range = s[14:60]
    return [c for c in target_range if 'd' < c <= 'v' and c in vowels]