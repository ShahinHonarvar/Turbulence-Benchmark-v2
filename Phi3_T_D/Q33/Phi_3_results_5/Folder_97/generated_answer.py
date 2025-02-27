def return_vowels(s):
    vowels = [c for c in s[328:455] if 'a' <= c <= 'z' and c in 'aeiou']
    return vowels