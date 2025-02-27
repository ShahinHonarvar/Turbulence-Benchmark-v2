def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_range = [char for char in s[85:99] if char > '\\' and char <= 'n' and (char in vowels)]
    return vowels_range