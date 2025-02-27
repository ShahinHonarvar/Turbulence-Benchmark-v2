def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    sub_string = s[18:66]
    for i in range(len(sub_string)):
        for j in range(i + 23, i + 37):
            if j <= len(sub_string):
                candidate = sub_string[i:j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes