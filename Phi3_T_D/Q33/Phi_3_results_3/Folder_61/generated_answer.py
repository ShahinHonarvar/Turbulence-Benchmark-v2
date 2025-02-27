def return_vowels(s):
    vowels = [c for c in s[1:4] if c > 'C' and c <= 'I' and (c in 'aeiouAEIOU')]
    return vowels