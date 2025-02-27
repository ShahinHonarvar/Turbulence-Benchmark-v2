def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [c for c in s[24:64] if c in vowels and 'F' < c <= 'H']
    return result