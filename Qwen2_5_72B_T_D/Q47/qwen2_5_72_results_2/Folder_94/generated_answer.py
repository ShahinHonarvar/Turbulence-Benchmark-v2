def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    subset = s[40:95]
    palindromes = set()
    for length in range(45, 52):
        for i in range(len(subset) - length + 1):
            candidate = subset[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes