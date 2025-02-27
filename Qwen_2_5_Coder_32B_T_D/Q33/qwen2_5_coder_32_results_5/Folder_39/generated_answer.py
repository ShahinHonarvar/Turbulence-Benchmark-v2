def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[32:97] if char > 'Q' and char <= ']' and (char in vowels)]