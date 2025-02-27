def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower)):
        for length in range(69, len(s_lower) - i + 1):
            if is_palindrome(s_lower[i:i + length]):
                palindromes.add(s_lower[i:i + length])
    return palindromes