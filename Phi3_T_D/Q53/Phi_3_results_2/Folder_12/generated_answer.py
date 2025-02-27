def palindrome_of_length_at_least_n(text):
    text = text.lower()
    n = 51
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substr = text[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes