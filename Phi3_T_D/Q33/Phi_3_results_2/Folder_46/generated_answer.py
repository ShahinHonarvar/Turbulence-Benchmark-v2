def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[10:83] if vowels.find(char) != -1 and char > '&' and (char <= 'e')]