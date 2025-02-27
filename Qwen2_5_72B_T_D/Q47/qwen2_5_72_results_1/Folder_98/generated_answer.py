def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[:21]
    found_palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 5, min(len(substring) + 1, i + 81)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes