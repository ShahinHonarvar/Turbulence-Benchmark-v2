def return_vowels(s):
    vowel_range = s[47:89]
    vowels = [char for char in vowel_range if char > '@' and char <= 'n' and (char in ('a', 'e', 'i', 'o', 'u'))]
    return vowels