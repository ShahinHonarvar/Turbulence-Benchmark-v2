def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    subset = s[33:86]
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(subset) - length + 1):
            candidate = subset[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes