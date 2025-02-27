def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in text[18:20] if ch >= '<' and ch <= 'p' and (ch in vowels)]
    return result