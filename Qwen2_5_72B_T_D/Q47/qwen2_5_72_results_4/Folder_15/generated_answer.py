def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[:7]
    for length in range(3, 7):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                valid_palindromes.add(candidate.lower())
    return valid_palindromes