def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[51:77] if c in vowels and c > '4' and (c <= '=')]