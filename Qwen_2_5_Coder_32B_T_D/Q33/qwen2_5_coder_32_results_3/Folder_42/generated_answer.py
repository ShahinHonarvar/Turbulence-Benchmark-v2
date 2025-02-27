def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[12:39] if char > ';' and char <= '|' and (char in vowels)]
    return result