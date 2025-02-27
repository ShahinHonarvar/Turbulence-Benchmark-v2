def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[1:4] if char in vowels and 'C' < char <= 'I']
    return result