def return_vowels(s):
    vowels = [char for char in s[1:9] if char in 'aeiou' and char > '?' and (char <= 'k')]
    return vowels