def palindrome_of_length_at_least_n(s):
    n = 85

    def is_palindrome(word):
        return word == word[::-1] and all((c.isalpha() for c in word))
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s_lower[i:j]):
                palindromes.add(s_lower[i:j])
    return palindromes