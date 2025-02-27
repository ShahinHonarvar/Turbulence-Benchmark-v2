def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[3:301]
    result = set()
    for i in range(len(s)):
        for j in range(i + 30, min(len(s), i + 301)):
            candidate = s[i:j + 1]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                result.add(candidate)
    return result