def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 46
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if is_palindrome(sub.lower()) and sub.isalpha():
                palindromes.add(sub)
    return palindromes