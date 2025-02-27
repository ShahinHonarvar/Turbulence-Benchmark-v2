def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', '{']
    return [c for c in s[17:64] if c in vowels and 'U' < c <= '{']