def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[15:90]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 40, min(i + 73, len(s) + 1)):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes