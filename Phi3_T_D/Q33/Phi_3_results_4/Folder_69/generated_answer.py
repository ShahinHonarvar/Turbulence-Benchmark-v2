def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [char for char in s[641:872] if char in vowels and '>' < char <= 'q']