def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[142:145] if c in vowels and c > 'd' and (c <= 'o')]