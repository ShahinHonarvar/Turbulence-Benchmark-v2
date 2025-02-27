def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[10:97] if c in vowels and 'R' < c <= 'b']