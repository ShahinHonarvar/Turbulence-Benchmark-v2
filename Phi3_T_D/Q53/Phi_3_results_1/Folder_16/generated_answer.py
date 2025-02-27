def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)

    def is_valid_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length - 118):
        for j in range(i + 119, length + 1):
            substr = s[i:j]
            if is_valid_palindrome(substr):
                palindromes.add(substr)
    return palindromes