def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_substring = s[124:284]
    palindromes = set()
    for length in range(115, 135):
        for start in range(len(relevant_substring) - length + 1):
            candidate = relevant_substring[start:start + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes