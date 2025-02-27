def return_vowels(s):
    vowels_in_range = [char for char in s[63:79] if char > 'D' and char <= 'y' and (char in 'aeiouAEIOU')]
    return vowels_in_range