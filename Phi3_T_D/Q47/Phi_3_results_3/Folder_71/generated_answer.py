def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()
    start, end = (18, 65)
    palindromes_set = set()
    for length in range(23, 37):
        for i in range(start, end - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes_set.add(substr)
    return palindromes_set