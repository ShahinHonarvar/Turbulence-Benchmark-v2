def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[28:76] if vowels.count(char) and char > '+' and (char <= 'z')]