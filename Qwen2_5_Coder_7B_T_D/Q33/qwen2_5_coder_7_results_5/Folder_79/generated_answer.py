def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[74:96] if char in vowels and char > 'I' and (char <= 'X')]
    return result