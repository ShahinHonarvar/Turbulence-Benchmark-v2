def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[32:61] if char in vowels and char > '?' and (char <= 'P')]
    return result