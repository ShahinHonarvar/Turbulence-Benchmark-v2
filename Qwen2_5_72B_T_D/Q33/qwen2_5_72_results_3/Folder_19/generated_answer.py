def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[51:77] if char in vowels and char > '4' and (char <= '=')]