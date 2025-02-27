def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[63:79] if char in vowels and char > 'D' and (char <= 'y')]
    return result