def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[64:82] if ch.lower() in vowels and 'P' < ch <= 'z']