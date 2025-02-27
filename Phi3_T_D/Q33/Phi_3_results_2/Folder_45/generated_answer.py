def return_vowels(s):
    vowels = frozenset('aeiou')
    result = [c for c in s[43:70] if '*' < c <= 'b' and c in vowels]
    return result