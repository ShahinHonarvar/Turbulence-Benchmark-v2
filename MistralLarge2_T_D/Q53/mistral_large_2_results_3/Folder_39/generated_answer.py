def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 69
    palindromes = set()
    s_lower = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s_lower[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(s[i:j])
    return palindromes