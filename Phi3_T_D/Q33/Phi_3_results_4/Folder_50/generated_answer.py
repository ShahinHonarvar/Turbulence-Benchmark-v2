def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start, end = (11, 53)
    return [c for c in s[start:end] if c in vowels and 'G' < c <= 'W']