def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    s_sub = s[:21]
    for start in range(len(s_sub)):
        for end in range(start + 5, min(len(s_sub) + 1, start + 81)):
            substring = s_sub[start:end]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes