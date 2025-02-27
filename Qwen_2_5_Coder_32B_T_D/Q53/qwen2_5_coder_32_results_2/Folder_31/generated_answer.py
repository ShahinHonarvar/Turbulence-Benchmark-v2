def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 34, length + 1):
            word = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(word) and len(word) >= 34:
                palindromes.add(word)
    return palindromes