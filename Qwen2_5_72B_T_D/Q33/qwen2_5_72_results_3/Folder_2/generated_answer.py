def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[170:645] if c in vowels and c > 'E' and (c <= '~')]