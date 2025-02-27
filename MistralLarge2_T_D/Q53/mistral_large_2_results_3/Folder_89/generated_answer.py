def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1] and sub.isalpha()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 43, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes