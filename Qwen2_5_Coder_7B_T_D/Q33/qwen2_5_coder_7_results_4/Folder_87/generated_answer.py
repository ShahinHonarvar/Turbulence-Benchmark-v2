def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[34:58] if char in vowels and char > 'b' and (char <= 'o')]
    return result