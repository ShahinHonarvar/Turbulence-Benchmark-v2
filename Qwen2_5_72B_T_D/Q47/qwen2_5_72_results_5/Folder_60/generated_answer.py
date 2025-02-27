def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    sub_string = s[23:83]
    valid_palindromes = set()
    for length in range(32, 35):
        for start in range(len(sub_string) - length + 1):
            candidate = sub_string[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes