def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[1:9] if ch in vowels]
    return [ch for ch in result if ch > '?' and ch <= 'k']