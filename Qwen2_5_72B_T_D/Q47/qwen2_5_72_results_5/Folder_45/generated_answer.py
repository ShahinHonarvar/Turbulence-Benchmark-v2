def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for i in range(70, 141):
        for j in range(i + 3, min(141, i + 61)):
            candidate = s[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result