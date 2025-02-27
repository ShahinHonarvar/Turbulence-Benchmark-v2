def palindrome_of_length_at_least_n(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 18, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes