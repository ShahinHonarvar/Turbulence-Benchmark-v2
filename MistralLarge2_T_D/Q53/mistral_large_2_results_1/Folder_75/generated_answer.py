def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = ''.join((char for char in s if char.isalpha())).lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 40, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes