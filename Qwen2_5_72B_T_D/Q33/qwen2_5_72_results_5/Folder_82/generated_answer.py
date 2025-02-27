def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[86:99] if ch.lower() in vowels and 'E' < ch <= 'r']