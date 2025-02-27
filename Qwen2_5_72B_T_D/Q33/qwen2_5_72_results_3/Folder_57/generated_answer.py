def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[21:23] if char > '-' and char <= 'n' and (char in vowels)]
    return result