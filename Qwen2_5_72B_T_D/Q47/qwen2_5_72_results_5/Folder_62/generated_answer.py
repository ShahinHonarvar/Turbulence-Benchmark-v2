def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    specified_substring = s[26:88]
    result = set()
    for length in range(52, 57):
        for i in range(len(specified_substring) - length + 1):
            candidate = specified_substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result