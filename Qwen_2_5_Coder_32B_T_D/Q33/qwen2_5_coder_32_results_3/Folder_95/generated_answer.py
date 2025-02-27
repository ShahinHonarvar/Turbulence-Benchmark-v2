def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[32:61] if char > '?' and char <= 'P' and (char in vowels)]