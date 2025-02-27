def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[13:37] if char in vowels and char > 'Z' and (char <= '}')]