def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 48, n + 1):
            substr = s[i:j]
            if is_palindrome(substr.lower()) and substr.isalpha():
                palindromes.add(substr)
    return palindromes