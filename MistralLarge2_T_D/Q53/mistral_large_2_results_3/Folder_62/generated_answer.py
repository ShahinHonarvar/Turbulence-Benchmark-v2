def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 31, length + 1):
            sub = s[i:j].lower()
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes