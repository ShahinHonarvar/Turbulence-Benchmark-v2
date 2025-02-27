def return_vowels(text):
    vowels = {'e', 'i', 'o', 'u'}
    return [char for char in text[27:57] if char in vowels and char > 'o' and (char <= 'w')]