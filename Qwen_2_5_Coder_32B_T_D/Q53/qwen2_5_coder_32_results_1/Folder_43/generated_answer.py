def palindrome_of_length_at_least_n(s):

    def is_palindrome(w):
        return w == w[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 48):
        for j in range(i + 49, len(s) + 1):
            word = ''.join(filter(str.isalpha, s[i:j]))
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes