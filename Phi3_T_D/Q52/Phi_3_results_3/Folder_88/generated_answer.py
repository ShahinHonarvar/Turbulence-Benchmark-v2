def palindrome_of_length_n(text):
    clean_text = ''.join(filter(str.isalpha, text)).lower()
    palindromes = {clean_text[i:i + 13] for i in range(len(clean_text) - 12)}
    return {p for p in palindromes if p == p[::-1]}