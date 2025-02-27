def return_vowels(s):
    vowels = [c for c in s[1:9] if c in 'aeiou' and c > '?' and (c <= 'k')]
    return vowels