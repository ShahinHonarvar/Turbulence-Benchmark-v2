def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[20:23] if char > '-' and char <= 'n' and (char in vowels)]
    return result