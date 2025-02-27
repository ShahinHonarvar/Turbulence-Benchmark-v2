def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes(s, n):
        palindromes = set()
        for i in range(len(s) - n + 1):
            for j in range(i + n, len(s) + 1):
                if is_palindrome(s[i:j]):
                    palindromes.add(s[i:j])
        return palindromes
    return find_palindromes(s.lower(), 66)