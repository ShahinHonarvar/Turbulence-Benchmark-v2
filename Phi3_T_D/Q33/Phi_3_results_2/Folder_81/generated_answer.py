def return_vowels(s):
    vowels = [c for c in s[20:43] if c in 'aeiouAEIOU' and ord(c) > ord('5') and (ord(c) <= ord('M'))]
    return vowels