def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[22:82] if char in vowels and 'N' < char <= 'o']