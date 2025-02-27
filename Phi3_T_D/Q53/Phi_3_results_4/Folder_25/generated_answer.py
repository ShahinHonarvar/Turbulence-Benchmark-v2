def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    s = list(filter(str.isalpha, s.lower()))
    n = 38
    length = len(s)
    palindromes = set()
    for i in range(length - n + 1):
        for size in range(n, length - i + 1):
            substring = ''.join(s[i:i + size])
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes