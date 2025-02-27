def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[34:69] if char in vowels and char > '_' and (char <= 'o')]
    return result