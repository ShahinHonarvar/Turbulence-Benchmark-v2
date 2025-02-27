def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[2:7] if ch in vowels and '^' < ch <= 'd']
    return result