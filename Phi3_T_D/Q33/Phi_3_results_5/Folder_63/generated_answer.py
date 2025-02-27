def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in text[34:69] if char in vowels and 'a' < char <= 'o']
    return result