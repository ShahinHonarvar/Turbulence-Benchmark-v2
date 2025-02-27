def return_vowels(s, q, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [c for c in s[1:9] if c in vowels and q < c <= k]
    return result