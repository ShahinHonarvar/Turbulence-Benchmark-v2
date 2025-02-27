def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for length in range(62, len(s) - i + 1):
            word = s[i:i + length]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes