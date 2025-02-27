def return_vowels(s):
    vowels = [c for c in s[15:86] if c in 'aeiouAEIOU' and '@' < c <= '~']
    return vowels