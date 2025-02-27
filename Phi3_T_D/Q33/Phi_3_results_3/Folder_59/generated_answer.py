def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[8:10] if ch in vowels and 'y' < ch <= 's']
    return result