def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[202:872] if c in vowels and 3 < ord(c) <= ord('>')]