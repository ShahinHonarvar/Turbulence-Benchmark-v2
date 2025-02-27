def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[32:97] if char.lower() in vowels and 'Q' < char <= ']']