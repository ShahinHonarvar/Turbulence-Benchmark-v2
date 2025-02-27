def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for ch in s[11:53] if ch in vowels and ch > '+' and (ch <= 'W')]
    return result