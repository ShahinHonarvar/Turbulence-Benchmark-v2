def palindrome_of_length_n(text):
    text = text.lower()
    n = 42
    return {text[i:i + n] for i in range(len(text) - n + 1) if text[i:i + n] == text[i:i + n][::-1]}