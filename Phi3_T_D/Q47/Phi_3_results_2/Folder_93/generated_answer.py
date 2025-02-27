def palindromes_of_specific_lengths(s):
    sub_str = s[17:96]
    palindrome_set = set()
    n = len(sub_str)
    for length in range(13, 50):
        for i in range(n - length + 1):
            potential_palindrome = sub_str[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                palindrome_set.add(potential_palindrome.lower())
    return palindrome_set