def return_vowels(text):
    start = 19
    end = 32
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[start:end] if char in vowels]