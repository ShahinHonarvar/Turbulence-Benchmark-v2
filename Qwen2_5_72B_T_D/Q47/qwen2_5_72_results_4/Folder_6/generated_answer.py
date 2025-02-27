def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    result = set()
    substring = s[45:99]
    for i in range(len(substring)):
        for j in range(i + 40, i + 48):
            if j <= len(substring):
                candidate = substring[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result