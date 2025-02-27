def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in s[56:96] if char in vowels and char > '&' and (char <= 'T')]
    return filtered_vowels