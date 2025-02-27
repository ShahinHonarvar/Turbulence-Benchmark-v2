def return_vowels(s):
    vowels = [c for c in s[34:69] if c > '_' and c <= 'o' and (c in 'aeiouAEIOU')]
    return vowels