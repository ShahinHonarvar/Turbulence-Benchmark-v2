def return_vowels(s: str) -> list:
    return [c for c in s[15:86] if 'a' <= c <= 'z' and c in 'aeiou']