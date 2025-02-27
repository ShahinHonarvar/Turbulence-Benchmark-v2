def return_vowels(s):
    start, end = (56, 68)
    vowels = 'aeiou'
    result = [ch for ch in s[start:end] if ch in vowels and 'm' < ch <= 'x']
    return result