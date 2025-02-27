def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s = s[:7]
    for length in range(3, 7):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring.lower())
    return valid_palindromes