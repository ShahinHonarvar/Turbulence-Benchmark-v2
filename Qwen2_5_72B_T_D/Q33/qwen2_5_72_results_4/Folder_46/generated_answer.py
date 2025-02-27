def return_vowels(s):
    vowels = 'aeiou'
    filtered_vowels = [char for char in s[10:83] if char in vowels and '%' < char <= 'e']
    return filtered_vowels