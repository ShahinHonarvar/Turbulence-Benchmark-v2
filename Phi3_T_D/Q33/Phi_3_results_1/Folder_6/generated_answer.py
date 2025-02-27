def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[20:34] if 'u' < char <= 'i' and char in vowels]
    return result