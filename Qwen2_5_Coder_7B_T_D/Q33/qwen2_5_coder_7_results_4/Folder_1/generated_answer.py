def return_vowels(s):
    vowels = [char for char in s[24:64] if char in 'aeiou' and char > 'F' and (char <= 'h')]
    return vowels