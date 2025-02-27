def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 87, n + 1):
            candidate = s[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes