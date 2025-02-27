def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()
    for i in range(n):
        for j in range(i + 29, n + 1):
            substring = text[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes