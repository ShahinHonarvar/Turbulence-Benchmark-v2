def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[12:123]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 12, min(len(s) + 1, start + 221)):
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes