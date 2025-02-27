def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[90:97] if ch in vowels and ch > '_' and (ch <= 'x')]
    return result