def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 13, length):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes