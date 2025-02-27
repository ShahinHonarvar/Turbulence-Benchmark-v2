def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 80
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr.isalpha() and is_palindrome(substr) and (len(substr) >= n):
                palindromes.add(substr)
    return palindromes