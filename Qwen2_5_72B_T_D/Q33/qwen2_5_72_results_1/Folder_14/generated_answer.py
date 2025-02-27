def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[47:61] if c > '9' and c <= 'O' and (c in vowels)]
    return result