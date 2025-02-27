def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    for start in range(30, 96):
        for end in range(start + 33, min(start + 56, 96), 1):
            substring = s[start:end + 1]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes