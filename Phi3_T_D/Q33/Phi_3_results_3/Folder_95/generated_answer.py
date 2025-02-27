def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[32:61] if 90 > ord(c) > 82 and c in vowels]