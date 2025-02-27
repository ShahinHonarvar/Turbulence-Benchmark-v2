def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[13:37] if char.lower() in vowels and 'Z' < char <= '}']