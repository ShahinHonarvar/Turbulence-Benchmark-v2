def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[130:296]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 103, min(start + 159, len(s) + 1)):
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes