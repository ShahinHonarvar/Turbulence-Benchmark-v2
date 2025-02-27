def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 87, len(s) + 1):
            candidate = s[i:j]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes