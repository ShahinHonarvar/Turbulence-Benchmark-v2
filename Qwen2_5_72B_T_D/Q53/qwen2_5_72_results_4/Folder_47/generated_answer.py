def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(s):
        return s == s[::-1]
    length = len(text)
    palindromes = set()
    for i in range(length):
        for j in range(i + 76, length + 1):
            candidate = text[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes