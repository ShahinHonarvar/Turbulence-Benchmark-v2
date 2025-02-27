def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[34:69] if char in vowels and '_' < char <= 'o']