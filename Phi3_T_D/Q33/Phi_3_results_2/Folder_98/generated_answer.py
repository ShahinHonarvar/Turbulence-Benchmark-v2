def return_vowels(s):
    vowels = [c for c in s[3:9] if c in 'aeiou']
    return [v for v in vowels if 'u' >= v >= 's']