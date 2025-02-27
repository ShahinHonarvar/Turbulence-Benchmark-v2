def palindrome_of_length_n(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 337):
        substring = text[i:i + 338]
        if all((c in alphabet for c in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes