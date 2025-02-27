def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 55, len(s) + 1):
            word = s[i:j]
            if word.isalpha() and is_palindrome(word):
                palindromes.add(word)
    return palindromes