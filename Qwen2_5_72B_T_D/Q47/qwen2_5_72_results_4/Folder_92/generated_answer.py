def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    subset = s[0:5]
    palindromes = set()
    for length in (3, 4):
        for i in range(len(subset) - length + 1):
            sub = subset[i:i + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes