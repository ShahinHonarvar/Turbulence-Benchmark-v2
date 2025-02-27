def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[328:455] if char in vowels and char > '<' and (char <= 'z')]