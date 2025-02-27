def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[604:949] if char.lower() in vowels and 'N' < char <= 'U']