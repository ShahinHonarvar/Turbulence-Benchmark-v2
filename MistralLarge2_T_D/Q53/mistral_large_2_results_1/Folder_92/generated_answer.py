def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 10, length + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes