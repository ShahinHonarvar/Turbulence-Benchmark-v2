def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[15:96]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 20, min(start + 67, len(substring) + 1)):
            sub = substring[start:end]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes