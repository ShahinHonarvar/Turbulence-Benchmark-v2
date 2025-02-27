def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[26:88]
    palindromes = set()
    for length in range(52, 57):
        for start in range(len(specified_substring) - length + 1):
            sub = specified_substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes