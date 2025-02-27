def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 70, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= 70 and substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes