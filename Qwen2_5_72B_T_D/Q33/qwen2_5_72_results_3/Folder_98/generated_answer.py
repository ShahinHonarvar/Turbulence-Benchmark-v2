def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for char in s[3:9] if char in vowels and 'S' < char <= 'U']
    return result