def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[10:97] if char in vowels and char > 'R' and (char <= 'b')]