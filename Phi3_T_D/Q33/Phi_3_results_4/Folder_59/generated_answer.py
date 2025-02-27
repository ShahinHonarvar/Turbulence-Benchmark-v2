def return_vowels(s):
    vowels = 'aeiou'
    return [letter for letter in s[8:9] if letter in vowels and ord('Y') < ord(letter) <= ord('s')]