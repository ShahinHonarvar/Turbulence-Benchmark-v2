def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 98, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes