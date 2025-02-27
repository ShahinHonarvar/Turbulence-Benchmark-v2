def return_vowels(s):
    vowels = ['e', 'i', 'o', 'u']
    result = [ch for ch in s[24:64] if ch in vowels and ch > 'F' and (ch <= 'h')]
    return result