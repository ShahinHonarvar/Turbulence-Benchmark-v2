def return_vowels(text):
    vowels = [char for char in text[36:56] if 9 + 1 <= ord(char) <= 47]
    return [char for char in vowels if char in 'aeiouAEIOU']