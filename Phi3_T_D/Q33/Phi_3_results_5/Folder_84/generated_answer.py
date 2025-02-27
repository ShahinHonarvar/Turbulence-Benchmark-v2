def return_vowels(s):
    start, end = (770, 852)
    range_str = s[start:end]
    return [ch for ch in range_str if 'A' <= ch <= 'I' and ch in 'AEIOUaeiou']