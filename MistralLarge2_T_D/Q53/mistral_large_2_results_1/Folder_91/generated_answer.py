def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 7, length + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes