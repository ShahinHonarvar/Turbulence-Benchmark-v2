def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[40:94] if c in vowels and 'e' < c <= 'H']