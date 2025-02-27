def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[528:606] if c in vowels and 'M' < c <= 'X']