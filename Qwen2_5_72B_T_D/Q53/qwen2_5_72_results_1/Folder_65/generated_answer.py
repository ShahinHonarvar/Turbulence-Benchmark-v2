def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()
    for i in range(n):
        for j in range(i + 14, n):
            segment = text[i:j + 1]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes