def return_vowels(s):
    vowels = [char for char in s[40:91] if char in 'AEIOUaeiou' and 'A' < char <= 'x']
    return vowels