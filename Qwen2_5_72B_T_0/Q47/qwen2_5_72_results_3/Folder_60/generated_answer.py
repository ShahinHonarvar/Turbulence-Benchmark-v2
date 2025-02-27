def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes