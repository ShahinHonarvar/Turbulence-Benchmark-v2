def return_vowels(s):
    vowels = [char for char in s[1:4] if char > 'C' and char <= 'I']
    vowels_filtered = [char for char in vowels if char in 'AEIOUaeiou']
    return vowels_filtered