def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_valid_palindrome(pal):
        return len(pal) >= 12 and len(pal) <= 18 and pal.isalpha()
    substring = s[29:97]
    found_palindromes = set()
    for length in range(12, 19):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_valid_palindrome(candidate):
                found_palindromes.add(candidate.lower())
    return found_palindromes