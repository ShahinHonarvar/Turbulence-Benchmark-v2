def return_vowels(s):
    vowels = 'aeiouAEIOU'
    valid_chars = [c for c in s[323:526] if c in vowels and c > '+' and (c <= ':')]
    return valid_chars