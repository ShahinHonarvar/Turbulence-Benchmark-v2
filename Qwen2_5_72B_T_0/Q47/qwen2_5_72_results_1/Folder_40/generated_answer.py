def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[:6]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(len(s) + 1, i + 6)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes