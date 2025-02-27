def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[15:86] if c in vowels and '@' < c <= '~']