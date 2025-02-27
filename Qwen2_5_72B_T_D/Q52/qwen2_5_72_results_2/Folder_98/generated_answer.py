def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 5):
        substring = text[i:i + 6]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes