def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[529:828] if vowels.count(char) > 0 and 'U' < char <= 'l']
    return result