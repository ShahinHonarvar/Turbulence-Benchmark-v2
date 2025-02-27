def return_vowels(s):
    vowels_range = s[34:58]
    vowels = [c for c in vowels_range if 'a' <= c <= 'o' and c not in ('b', 'c', 'd')]
    return vowels