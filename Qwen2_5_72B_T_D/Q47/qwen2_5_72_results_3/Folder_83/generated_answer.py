def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    subset = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(subset) - length + 1):
            sub = subset[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes