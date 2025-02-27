def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[37:57] if '*' < char <= 'P' and char in vowels]
    return result