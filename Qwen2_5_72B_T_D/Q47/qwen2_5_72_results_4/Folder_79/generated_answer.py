def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[1:9].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes