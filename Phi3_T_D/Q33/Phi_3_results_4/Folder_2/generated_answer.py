def return_vowels(s):
    vowels = [c for c in s[170:645] if 'F' <= c <= '~' and c in 'aeiouAEIOU']
    return vowels