def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[31:37] if '`' <= char <= 't' and char in vowels]
    return result