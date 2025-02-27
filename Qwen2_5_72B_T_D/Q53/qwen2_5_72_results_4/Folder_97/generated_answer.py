def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    n = 138
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes