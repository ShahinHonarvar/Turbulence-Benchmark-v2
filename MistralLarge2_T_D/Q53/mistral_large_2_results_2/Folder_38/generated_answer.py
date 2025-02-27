def palindrome_of_length_at_least_n(s):

    def is_palindrome(string):
        return string == string[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 56, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes