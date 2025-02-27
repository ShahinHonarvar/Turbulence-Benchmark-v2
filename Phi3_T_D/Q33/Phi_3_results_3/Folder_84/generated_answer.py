def return_vowels(s):
    vowels = [char for char in s[770:852] if char > 'B' and char <= 'i' and (char in 'aeiou')]
    return vowels