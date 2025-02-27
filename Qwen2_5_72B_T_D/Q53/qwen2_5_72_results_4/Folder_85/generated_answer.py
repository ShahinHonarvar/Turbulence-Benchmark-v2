def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 84, len(s)):
            candidate = s[i:j + 1]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes