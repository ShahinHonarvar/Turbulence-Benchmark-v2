def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[8:9] if char.lower() in vowels and 'Y' < char <= 's']