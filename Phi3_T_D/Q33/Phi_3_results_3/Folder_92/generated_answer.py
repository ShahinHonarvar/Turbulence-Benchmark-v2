def return_vowels(s):
    vowels = [char for char in s[3:8] if char > ';' and char <= 'D' and (char in 'aeiouAEIOU')]
    return vowels