def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[32:97] if char in vowels and char > 'Q' and (char <= ']')]