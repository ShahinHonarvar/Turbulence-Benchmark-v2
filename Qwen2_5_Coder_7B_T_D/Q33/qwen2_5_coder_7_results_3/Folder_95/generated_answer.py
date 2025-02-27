def return_vowels(s):
    return [char for char in s[32:61] if char in 'aeiou' and char > '?' and (char <= 'P')]