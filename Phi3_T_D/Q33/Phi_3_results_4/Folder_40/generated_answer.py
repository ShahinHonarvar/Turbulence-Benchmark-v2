def return_vowels(text):
    vowels = ['e', 'i', 'o', 'u']
    result = [ch for ch in text[2:7] if ch in vowels and '^' < ch <= 'd']
    return result