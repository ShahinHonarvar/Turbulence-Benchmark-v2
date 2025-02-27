def return_vowels(text):
    result = [ch for ch in text[604:949] if ch in 'AEIOUaeiou' and 'N' < ch <= 'U']
    return result