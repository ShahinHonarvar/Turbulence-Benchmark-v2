def return_vowels(s):
    vowels = 'aeiou'
    filtered_chars = [char for char in s[15:86] if '@' < char <= '~' and char in vowels]
    return filtered_chars