def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[3:8] if char.lower() in vowels and ';' < char <= 'D']