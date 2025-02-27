def return_vowels(s):
    vowels = 'AEIOU'
    filtered_vowels = [char for char in s[74:96] if char in vowels and 'I' < char <= 'X']
    return filtered_vowels