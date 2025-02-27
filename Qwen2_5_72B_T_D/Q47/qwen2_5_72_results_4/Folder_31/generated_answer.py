def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    subset = s[11:84]
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 36, min(84, i + 61)):
            candidate = subset[i - 11:j - 11]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes