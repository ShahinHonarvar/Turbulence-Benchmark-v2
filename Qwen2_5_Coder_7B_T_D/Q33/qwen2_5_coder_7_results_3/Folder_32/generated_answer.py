def return_vowels(s):
    vowels = [char for char in s[45:76] if char in 'aeiou' and char > 'b' and (char <= 'z')]
    return vowels