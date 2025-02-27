def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[29:73] if char in vowels and char > '#' and (char <= '.')]
    return result