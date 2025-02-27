def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + 57, length + 1):
            substr = s[i:j]
            if is_palindrome(substr) and substr.isalpha():
                palindromes.add(substr)
    return palindromes