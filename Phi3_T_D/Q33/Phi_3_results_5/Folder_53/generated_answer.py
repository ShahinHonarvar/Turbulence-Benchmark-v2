def return_vowels(s):
    vowels = [char for char in s[26:57] if 'o' < char <= 'w' and char in 'aeiou']
    return vowels