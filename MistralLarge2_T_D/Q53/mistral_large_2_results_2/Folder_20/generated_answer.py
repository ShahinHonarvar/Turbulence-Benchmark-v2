def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 66, length + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring.lower())
    return palindromes