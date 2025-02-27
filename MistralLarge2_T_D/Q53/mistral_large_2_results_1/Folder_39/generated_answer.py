def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 69
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if is_palindrome(substr) and substr.isalpha():
                palindromes.add(substr)
    return palindromes