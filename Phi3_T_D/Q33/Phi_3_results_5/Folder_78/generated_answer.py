def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[46:90] if '@' < char <= '[' and char in vowels]
    return result