def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(63, 71):
        for j in range(i + 4, i + 6):
            for k in range(i, len(string) - j + i + 1):
                substring = string[k:k + j - i]
                if is_palindrome(substring) and substring.isalpha():
                    palindromes.add(substring)
    return palindromes