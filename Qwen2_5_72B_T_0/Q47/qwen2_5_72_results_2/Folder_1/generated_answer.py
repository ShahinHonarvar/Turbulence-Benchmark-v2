def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_range = s[15:90]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 40, min(start + 73, len(valid_range) + 1)):
            substring = valid_range[start:end]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes