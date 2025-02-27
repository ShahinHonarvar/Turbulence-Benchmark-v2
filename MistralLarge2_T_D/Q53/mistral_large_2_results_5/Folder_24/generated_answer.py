def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 53, length + 1):
            sub = s[i:j].lower()
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes