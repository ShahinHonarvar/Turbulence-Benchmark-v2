def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[22:82] if ch in vowels and 'N' < ch <= 'o']