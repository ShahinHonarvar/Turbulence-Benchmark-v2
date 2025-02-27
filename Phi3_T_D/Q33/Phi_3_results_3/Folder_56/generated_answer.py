def return_vowels(s):
    return [ch for ch in s[15:86] if 'aeiou'.find(ch) >= 0 and '@' < ch <= '~']