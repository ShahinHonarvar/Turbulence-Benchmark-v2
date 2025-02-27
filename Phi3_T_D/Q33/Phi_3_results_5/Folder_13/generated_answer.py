def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[149:313] if vowels.find(char) != -1 and ord('M') < ord(char) <= ord('j')]