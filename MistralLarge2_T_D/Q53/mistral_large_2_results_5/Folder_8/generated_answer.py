def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    n = 45
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes