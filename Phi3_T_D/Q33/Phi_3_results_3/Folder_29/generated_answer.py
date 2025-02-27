def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in text[19:20] if ch.lower() in vowels and ord(ch) > ord('<') and (ord(ch) <= ord('p'))]