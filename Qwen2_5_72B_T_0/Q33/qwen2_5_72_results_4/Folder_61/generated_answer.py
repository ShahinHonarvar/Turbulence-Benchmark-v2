def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[1:4] if char.lower() in vowels and 'C' < char <= 'I']