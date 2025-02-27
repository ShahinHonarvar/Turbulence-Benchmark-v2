def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[63:79] if ch in vowels and 'd' < ch <= 'y']
    return result