def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 68, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes