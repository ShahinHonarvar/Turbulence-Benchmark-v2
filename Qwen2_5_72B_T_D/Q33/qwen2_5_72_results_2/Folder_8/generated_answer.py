def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[64:82] if char.lower() in vowels and 'P' < char <= 'z']