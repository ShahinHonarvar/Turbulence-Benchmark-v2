def return_vowels(s):
    vowels = [char for char in s[1:4] if char in 'aeiou' and char > 'C' and (char <= 'I')]
    return vowels