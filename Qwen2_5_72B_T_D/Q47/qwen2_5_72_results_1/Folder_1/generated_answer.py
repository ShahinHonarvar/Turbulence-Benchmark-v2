def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    target_substring = s[15:90]
    palindromes = set()
    for start in range(len(target_substring)):
        for end in range(start + 39, min(start + 73, len(target_substring))):
            candidate = target_substring[start:end + 1]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes