def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    specified_substring = s[24:98]
    palindromes_set = set()
    for i in range(len(specified_substring)):
        for j in range(i + 10, i + 37):
            if j <= len(specified_substring):
                candidate = specified_substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes_set.add(candidate.lower())
    return palindromes_set