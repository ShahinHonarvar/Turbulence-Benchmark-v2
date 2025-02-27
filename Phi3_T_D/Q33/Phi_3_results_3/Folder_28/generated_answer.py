def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [c for c in s[41:50] if c in vowels and 'W' < c <= '[']
    return result