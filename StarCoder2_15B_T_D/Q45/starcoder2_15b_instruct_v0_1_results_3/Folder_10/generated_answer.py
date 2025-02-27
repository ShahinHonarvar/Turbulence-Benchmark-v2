def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(len(s), i + 6) + 1):
            for k in range(i + 1, j):
                palindrome = s[i:k] + s[k:j][::-1]
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes