def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    sub_string = s[11:84]
    palindromes = set()
    for start in range(len(sub_string)):
        for end in range(start + 36, start + 61):
            if end < len(sub_string):
                candidate = sub_string[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate.lower())
    return palindromes