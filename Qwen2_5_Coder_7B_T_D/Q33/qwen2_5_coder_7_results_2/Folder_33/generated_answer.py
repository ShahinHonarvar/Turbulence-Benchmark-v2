def return_vowels(s):
    vowels = [c for i, c in enumerate(s[163:771]) if c in 'AEIOU' and c > ':' and (c <= 'E')]
    return vowels