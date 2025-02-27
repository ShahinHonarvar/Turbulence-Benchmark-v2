def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    subset = s[39:95]
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 14, min(i + 53, len(subset) + 1)):
            part = subset[i:j]
            if part.isalpha() and is_palindrome(part.lower()):
                palindromes.add(part)
    return palindromes