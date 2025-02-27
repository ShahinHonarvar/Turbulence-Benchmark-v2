def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[19:32] if '0' < char <= '7' and char in vowels]
    return result