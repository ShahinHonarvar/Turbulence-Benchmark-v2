def return_vowels(s):
    vowels = 'aeiouAEIOU'
    start, end = (37, 58)
    return [c for c in s[start:end] if '*' < c <= 'P' and c in vowels]