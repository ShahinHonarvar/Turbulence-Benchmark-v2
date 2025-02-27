def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + 5, length + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes