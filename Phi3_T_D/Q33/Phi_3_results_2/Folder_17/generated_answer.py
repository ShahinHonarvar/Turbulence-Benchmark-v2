def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[60:99] if ch in vowels and 'j' < ch <= 'n']
    return result