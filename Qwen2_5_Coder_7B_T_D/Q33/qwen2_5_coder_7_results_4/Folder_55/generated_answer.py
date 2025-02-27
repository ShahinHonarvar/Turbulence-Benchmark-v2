def return_vowels(s):
    vowels = [c for c in s[1:5] if c in 'aeiou' and '!' < c <= 'j']
    return vowels