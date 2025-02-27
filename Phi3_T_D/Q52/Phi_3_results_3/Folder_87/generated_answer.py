def palindrome_of_length_n(text):
    n = 57
    text = text.lower()
    palindromes = {text[i:i + n] for i in range(len(text) - n + 1) if text[i:i + n] == text[i:i + n][::-1] and text[i:i + n].isalpha()}
    return palindromes