def return_vowels(s):
    vowels = 'AEIOU'
    filtered_vowels = [char for char in s if char in vowels and ord(char) > ord('%') and (ord(char) <= ord('G')) and (65 <= ord(char) < 70)]
    return filtered_vowels