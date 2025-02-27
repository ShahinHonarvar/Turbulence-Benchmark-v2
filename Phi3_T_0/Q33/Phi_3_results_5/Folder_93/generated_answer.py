def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[54:82] if char in vowels and char > '&' and (char <= '@')]