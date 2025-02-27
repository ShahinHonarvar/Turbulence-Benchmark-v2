def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_chars = [char for char in text[36:56] if char in vowels and ord(char) > ord('+') and (ord(char) <= ord('/'))]
    return selected_chars