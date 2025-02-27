def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = 96
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            candidate = text[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes