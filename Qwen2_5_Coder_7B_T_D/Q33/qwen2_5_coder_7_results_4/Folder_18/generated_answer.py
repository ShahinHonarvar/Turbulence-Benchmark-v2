def return_vowels(s):
    vowels = [c for c in s[528:606] if c in 'aeiouAEIOU' and 'M' < c <= 'X']
    return vowels