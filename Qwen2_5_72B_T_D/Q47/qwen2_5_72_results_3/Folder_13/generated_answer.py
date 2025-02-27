def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_range = s[13:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(valid_range) - length + 1):
            substring = valid_range[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes