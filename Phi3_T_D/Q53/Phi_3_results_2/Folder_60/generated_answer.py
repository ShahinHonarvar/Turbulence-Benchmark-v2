def palindrome_of_length_at_least_n(text):
    text = text.lower()
    length = len(text)
    palindromes = set()
    for i in range(length):
        for j in range(i + 80, length + 1):
            substring = text[i:j]
            if len(substring) >= 80 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes