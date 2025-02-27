def return_vowels(s):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [c for c in s[23:85] if 'W' < c <= 'v' and c in vowels]
    return filtered_vowels