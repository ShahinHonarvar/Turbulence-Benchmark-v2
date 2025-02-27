def return_vowels(s):
    vowels = [char for char in s[20:43] if char in 'aeiouAEIOU' and char > '5' and (char <= 'M')]
    return vowels