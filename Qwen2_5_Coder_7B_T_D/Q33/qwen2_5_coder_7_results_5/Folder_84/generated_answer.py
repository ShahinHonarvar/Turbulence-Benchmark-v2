def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[770:852] if char in vowels and char > 'B' and (char <= 'i')]