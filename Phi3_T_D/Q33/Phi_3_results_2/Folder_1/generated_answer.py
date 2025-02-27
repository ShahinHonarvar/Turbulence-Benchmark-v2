def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[24:64] if ch in vowels and 'f' < ch <= 'h']
    return result