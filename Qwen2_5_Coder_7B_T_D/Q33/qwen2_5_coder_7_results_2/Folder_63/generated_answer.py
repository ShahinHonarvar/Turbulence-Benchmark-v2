def return_vowels(s):
    vowels = [char for char in s[34:69] if char in 'aeiou' and char > '_' and (char <= 'o')]
    return vowels