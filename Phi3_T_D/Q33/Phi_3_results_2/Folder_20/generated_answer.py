def return_vowels(s):
    start, end = (59, 61)
    vowels = 'aeiou'
    return [ch for ch in s[start:end] if 'g' < ch <= 'h' and ch in vowels]