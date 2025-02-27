def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    target_substring = s[28:95]
    palindromes = set()
    for i in range(len(target_substring)):
        for j in range(i + 38, i + 50):
            if j <= len(target_substring):
                candidate = target_substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes