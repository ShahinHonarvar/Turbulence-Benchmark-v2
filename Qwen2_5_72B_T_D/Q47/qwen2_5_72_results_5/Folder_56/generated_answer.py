def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[1:10].lower()
    found_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(len(s) + 1, i + 8)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes