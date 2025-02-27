def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    subset = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for start in range(len(subset) - length + 1):
            sub = subset[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes