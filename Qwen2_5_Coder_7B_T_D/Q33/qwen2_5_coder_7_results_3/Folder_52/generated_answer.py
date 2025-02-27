def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[24:68] if char in vowels and char > 'f' and (char <= '|')]