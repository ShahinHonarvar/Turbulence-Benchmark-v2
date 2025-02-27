def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[5:6] if ch > 'd' and ch <= '^'] if 'd' <= s[5] <= '^' else []