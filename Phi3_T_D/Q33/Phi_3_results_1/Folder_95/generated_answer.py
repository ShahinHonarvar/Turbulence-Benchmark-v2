def return_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [c for c in text[31:60] if c in vowels and '?' < c <= 'P']