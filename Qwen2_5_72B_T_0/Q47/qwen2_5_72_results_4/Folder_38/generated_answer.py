def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[18:88]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 37, min(start + 61, len(substring))):
            candidate = substring[start:end + 1]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes