def return_vowels(s):
    vowel_list = [c for c in s[529:828] if c > 'U' and c <= 'l' and (c in 'AEIOUaeiou')]
    return vowel_list