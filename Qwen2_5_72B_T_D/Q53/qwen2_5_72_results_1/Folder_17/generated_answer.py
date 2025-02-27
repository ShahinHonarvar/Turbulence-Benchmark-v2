def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    n = 36
    palindromes = set()
    for i in range(len(text_lower) - n + 1):
        for j in range(i + n, len(text_lower) + 1):
            substring = text_lower[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes