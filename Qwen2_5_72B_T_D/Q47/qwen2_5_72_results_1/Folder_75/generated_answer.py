def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[31:75]
    palindromes_set = set()
    for start in range(len(specified_substring)):
        for end in range(start + 22, start + 40):
            if end < len(specified_substring):
                candidate = specified_substring[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes_set.add(candidate)
    return palindromes_set