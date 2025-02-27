def return_vowels(s):
    vowels = [c for c in s[90:97] if c > '_' and c <= 'x' and (c.lower() in 'aeiou')]
    return vowels