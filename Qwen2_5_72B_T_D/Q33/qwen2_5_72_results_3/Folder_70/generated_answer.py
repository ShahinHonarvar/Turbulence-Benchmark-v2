def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[171:402] if c in vowels and 'I' < c <= 'k']