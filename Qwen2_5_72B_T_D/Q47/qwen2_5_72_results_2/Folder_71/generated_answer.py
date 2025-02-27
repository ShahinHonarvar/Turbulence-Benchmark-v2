def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    s = s[18:66].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 23, min(len(s), i + 37)):
            candidate = s[i:j + 1]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result