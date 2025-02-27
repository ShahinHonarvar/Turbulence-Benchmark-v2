def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[20:41] if ch in vowels and 'k' < ch <= 'z']