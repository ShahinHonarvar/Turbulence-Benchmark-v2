def return_vowels(text):
    vowels = [ch for ch in text[1:4] if ch > 'C' and ch <= 'I' and (ch in 'AEIOUaeiou')]
    return vowels