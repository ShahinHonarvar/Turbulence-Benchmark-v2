def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[100:301].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 50, i + 101):
            if j <= len(s):
                candidate = s[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result