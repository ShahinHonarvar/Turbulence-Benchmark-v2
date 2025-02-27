def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s = s[:21]
    for i in range(len(s)):
        for j in range(i + 5, min(len(s) + 1, i + 81)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes