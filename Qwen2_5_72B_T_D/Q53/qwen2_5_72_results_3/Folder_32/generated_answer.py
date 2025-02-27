def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindromes = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 70, n + 1):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 70 and p.isalpha()}