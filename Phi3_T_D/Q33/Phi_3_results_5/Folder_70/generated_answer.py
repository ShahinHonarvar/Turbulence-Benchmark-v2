def return_vowels(s):
    vowels = [c for c in s[171:402] if c > 'I' and c <= 'k' and (c in 'aeiouAEIOU')]
    return vowels