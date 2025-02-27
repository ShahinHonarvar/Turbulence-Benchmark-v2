def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [c for c in s[40:49] if c in vowels and 'W' < c <= '[']
    return result