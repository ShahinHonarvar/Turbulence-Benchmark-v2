def return_vowels(s):
    start, end = (13, 35)
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [i for i in s[start:end] if i in vowels and 'a' > i <= 'F']