def return_vowels(s):
    return [c for c in s[63:79] if c in 'aeiouAEIOU' and ord('d') < ord(c) <= ord('y')]