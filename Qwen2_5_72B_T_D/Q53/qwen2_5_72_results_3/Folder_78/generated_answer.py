def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 95, length):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes