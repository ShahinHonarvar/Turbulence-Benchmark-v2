def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[130:296]
    results = set()
    for start in range(len(s)):
        for end in range(start + 103, min(start + 159, len(s) + 1)):
            sub = s[start:end]
            if sub.isalpha() and is_palindrome(sub.lower()):
                results.add(sub)
    return results