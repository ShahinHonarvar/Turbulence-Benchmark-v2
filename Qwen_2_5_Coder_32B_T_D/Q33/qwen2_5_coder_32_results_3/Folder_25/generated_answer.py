def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[28:76] if char > '+' and char <= 'z' and (char in vowels)]