def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 94, n + 1):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes