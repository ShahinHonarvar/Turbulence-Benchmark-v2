def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[28:76] if ch in vowels and '+' < ch <= 'z']