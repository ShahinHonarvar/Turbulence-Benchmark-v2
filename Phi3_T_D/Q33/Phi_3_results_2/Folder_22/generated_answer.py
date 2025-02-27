def return_vowels(s):
    return [char for char in s[56:90] if 'a' <= char <= 'z' and char in 'aeiou' and (char > 'k') and (char <= 'z')]