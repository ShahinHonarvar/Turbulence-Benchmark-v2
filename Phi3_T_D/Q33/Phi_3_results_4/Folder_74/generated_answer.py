def return_vowels(s):
    vowels = 'aeiouAEIOU'
    ret = [char for char in s[69:82] if char in vowels and char > '[' and (char <= '~')]
    return ret