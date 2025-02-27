def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[31:75]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 23, i + 40):
            if j <= len(s):
                substring = s[i:j].lower()
                if substring.isalpha() and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes