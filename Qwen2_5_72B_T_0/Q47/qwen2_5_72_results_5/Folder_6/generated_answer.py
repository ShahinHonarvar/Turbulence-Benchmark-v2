def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes