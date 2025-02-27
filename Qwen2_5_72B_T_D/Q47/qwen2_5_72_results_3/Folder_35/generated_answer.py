def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    s = s[34:91].lower()
    for start in range(len(s)):
        for end in range(start + 13, min(start + 40, len(s))):
            candidate = s[start:end + 1]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result