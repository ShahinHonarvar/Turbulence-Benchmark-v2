def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    start, end = (125, 283)
    min_length, max_length = (109, 126)
    valid_palindromes = set()
    substring = text[start:end + 1]
    for i in range(len(substring)):
        for j in range(i + min_length, min(i + max_length + 1, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                valid_palindromes.add(candidate)
    return valid_palindromes