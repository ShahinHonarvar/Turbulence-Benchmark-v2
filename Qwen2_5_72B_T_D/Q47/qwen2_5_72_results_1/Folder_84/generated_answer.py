def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    relevant_substring = s[23:78]
    palindromes = set()
    for length in range(13, 41):
        for start in range(len(relevant_substring) - length + 1):
            sub = relevant_substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes