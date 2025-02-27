def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in string[23:85] if char in vowels and char > 'w' and (char <= 'v')]
    return filtered_vowels