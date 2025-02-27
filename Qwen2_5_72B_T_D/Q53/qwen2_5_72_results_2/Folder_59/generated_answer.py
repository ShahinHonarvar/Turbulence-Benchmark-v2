def palindrome_of_length_at_least_n(text):
    text = text.lower()
    text_length = len(text)
    palindromes = set()
    for i in range(text_length):
        for j in range(i + 20, text_length + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes