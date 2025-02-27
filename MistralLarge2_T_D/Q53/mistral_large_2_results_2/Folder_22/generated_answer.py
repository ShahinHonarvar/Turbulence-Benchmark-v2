def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    n = 97
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes