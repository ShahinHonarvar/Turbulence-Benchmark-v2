def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(s)):
        for length in range(63, len(s) - i + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes