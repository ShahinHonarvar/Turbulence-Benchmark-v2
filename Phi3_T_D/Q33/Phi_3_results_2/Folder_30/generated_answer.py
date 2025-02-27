def return_vowels(s):
    vowels = 'AEIOU'
    return [letter for letter in s[11:61] if 'M' < letter <= 'W' and letter in vowels]