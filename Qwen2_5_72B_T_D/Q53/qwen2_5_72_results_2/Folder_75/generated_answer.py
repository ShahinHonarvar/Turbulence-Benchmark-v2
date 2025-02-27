def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()
    for i in range(n):
        for j in range(i + 39, n):
            substr = text[i:j + 1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes