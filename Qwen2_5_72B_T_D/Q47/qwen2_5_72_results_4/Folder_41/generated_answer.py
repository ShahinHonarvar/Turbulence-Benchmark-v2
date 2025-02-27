def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[1:8]
    palindromes_set = set()
    for i in range(len(specified_substring)):
        for j in range(i + 3, i + 5):
            if j <= len(specified_substring) and specified_substring[i:j].isalpha():
                candidate = specified_substring[i:j]
                if is_palindrome(candidate):
                    palindromes_set.add(candidate.lower())
    return palindromes_set