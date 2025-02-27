def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[5:6] if c in vowels and ord(c) > 3 and (ord(c) <= 94)]