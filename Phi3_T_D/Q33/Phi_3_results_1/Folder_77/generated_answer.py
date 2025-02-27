def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[837:975] if char in vowels and char > 'n' and (char <= 'w')]
    return result