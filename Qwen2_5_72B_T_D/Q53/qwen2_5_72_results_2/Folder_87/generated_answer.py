def palindrome_of_length_at_least_n(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 17, length):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes