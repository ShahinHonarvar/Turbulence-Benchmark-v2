def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    ranged_string = s[15:73]
    candidates = set()
    for length in range(19, 56):
        for start in range(len(ranged_string) - length + 1):
            candidate = ranged_string[start:start + length].lower()
            if is_palindrome(candidate):
                candidates.add(candidate)
    return candidates