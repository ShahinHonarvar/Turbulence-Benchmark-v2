def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[14:60] if char in vowels and char > 'D' and (char <= 'v')]
    return result