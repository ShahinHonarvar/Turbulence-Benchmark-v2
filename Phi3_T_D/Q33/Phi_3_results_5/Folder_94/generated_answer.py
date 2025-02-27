def return_vowels(s):
    vowel_idx = {'A': 0, 'E': 1, 'I': 2, 'O': 4, 'U': 5}
    return [c for i, c in enumerate(s[40:94]) if c in vowel_idx and ord(c) > ord('4') and (ord(c) <= ord('H'))]