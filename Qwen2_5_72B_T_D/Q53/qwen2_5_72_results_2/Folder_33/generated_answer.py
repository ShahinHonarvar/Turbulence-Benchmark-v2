def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = 141
    length = len(text)
    palindromes = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes