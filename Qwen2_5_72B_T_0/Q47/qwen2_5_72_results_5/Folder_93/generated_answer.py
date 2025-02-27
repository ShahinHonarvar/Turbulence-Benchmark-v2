def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_range = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for start in range(len(valid_range) - length + 1):
            sub = valid_range[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes