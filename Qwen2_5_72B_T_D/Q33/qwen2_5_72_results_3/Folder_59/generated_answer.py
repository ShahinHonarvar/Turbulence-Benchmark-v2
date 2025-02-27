def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[8:9] if char > 'Y' and char <= 's' and (char in vowels)]
    return result