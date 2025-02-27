def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    considered_range = s[:101]
    for length in range(3, 16):
        for start in range(len(considered_range) - length + 1):
            sub = considered_range[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub.lower())
    return valid_palindromes