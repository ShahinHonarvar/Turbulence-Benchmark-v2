def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 78
    length = len(s)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if is_palindrome(substring.lower()) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes