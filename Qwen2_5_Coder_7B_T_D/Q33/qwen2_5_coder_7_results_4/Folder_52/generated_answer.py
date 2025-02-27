def return_vowels(s):
    vowels = [char for char in s[24:68] if char in 'aeiou' and char > 'f' and (char <= '|')]
    return vowels