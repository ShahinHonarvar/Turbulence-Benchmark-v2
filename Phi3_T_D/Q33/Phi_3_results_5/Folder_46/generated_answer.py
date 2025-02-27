def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [char for char in s[10:83] if char in vowels and char > '%' and (char <= 'e')]