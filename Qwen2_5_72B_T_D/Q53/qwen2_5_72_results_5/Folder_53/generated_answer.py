def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = len(text)
    palindromes = set()
    for i in range(n):
        for j in range(i + 63, n):
            if text[i:j + 1] == text[i:j + 1][::-1] and text[i:j + 1].isalpha():
                palindromes.add(text[i:j + 1])
    return palindromes