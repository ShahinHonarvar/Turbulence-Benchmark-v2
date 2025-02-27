def return_vowels(text):
    vowels = [c for c in text[50:51] if c.lower() in 'aeiou' and ord(c.lower()) > ord('a')]
    return vowels