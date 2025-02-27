def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [ch for ch in s[528:606] if 'M' < ch <= 'X' and ch in vowels]
    return result