def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[20:34] if char in vowels and char > 'U' and (char <= 'i')]
    return result