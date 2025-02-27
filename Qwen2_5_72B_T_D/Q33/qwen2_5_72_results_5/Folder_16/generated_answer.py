def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[133:306] if char in vowels and 'c' < char <= 'd']
    return result