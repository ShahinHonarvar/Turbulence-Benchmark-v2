def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 86, length + 1):
            candidate = s[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes