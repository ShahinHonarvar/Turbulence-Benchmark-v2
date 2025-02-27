def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 34, n + 1):
            substring = s[i:j]
            if is_palindrome(substring.lower()) and substring.isalpha():
                palindromes.add(substring)
    return palindromes