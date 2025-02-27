def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[19:32] if char in vowels and 0 < ord(char) - ord('a') <= 7]