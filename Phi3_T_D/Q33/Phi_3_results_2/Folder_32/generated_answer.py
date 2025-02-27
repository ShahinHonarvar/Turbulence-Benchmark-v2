def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    required_chars = [char for char in text[44:75] if char in vowels and 'b' < char <= 'z']
    return required_chars