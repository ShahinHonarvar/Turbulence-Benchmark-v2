def return_vowels(s):
    vowels = [c for c in s[170:645] if c in 'aeiou' and c > 'E' and (c <= '~')]
    return vowels