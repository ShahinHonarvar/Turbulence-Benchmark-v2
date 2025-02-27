def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[163:771] if ch > ':' and ch <= 'E' and (ch in vowels)]
    return result