def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    relevant_substring = s[26:85]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(relevant_substring) - length + 1):
            candidate = relevant_substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes