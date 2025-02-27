def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[29:73] if '#' < char <= '.' and char in vowels]