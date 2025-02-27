def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[10:71]
    result = set()
    for start in range(len(s)):
        for end in range(start + 24, min(start + 53, len(s) + 1)):
            sub = s[start:end]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result