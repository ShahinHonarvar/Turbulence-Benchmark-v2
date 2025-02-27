def palindromes_of_specific_lengths(text):
    start, end = (33, 85)
    palindromes_set = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(26, 32):
        for i in range(start, end - length + 2):
            candidate = text[i:i + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set