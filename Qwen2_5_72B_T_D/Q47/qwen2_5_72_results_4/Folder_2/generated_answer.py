def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[10:60]
    found_palindromes = set()
    for length in range(18, 37):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                found_palindromes.add(candidate.lower())
    return found_palindromes