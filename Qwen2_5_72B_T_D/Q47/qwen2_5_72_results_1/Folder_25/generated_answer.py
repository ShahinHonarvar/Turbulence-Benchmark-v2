def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    relevant_substring = s[26:85]
    found_palindromes = set()
    for length in range(30, 47):
        for start in range(len(relevant_substring) - length + 1):
            candidate = relevant_substring[start:start + length]
            if is_palindrome(candidate) and candidate.isalpha():
                found_palindromes.add(candidate)
    return found_palindromes