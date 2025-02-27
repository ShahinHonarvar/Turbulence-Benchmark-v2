def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()
    for i in range(n):
        for j in range(i + 41, n):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes