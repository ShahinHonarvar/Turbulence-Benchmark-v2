def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    for i in range(len(s)):
        for j in range(i + 16, len(s)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes