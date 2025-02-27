def return_vowels(s):
    start, end = (56, 90)
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[start:end] if char in vowels and char > 'k' and (char <= 'z')]