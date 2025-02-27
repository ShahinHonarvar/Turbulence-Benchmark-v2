def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[63:79] if char.lower() in vowels and 'D' < char <= 'y']