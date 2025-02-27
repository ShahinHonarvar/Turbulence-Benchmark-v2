def palindromes_of_specific_lengths(s):
    result_set = set()
    substring = s[16:95]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                result_set.add(potential_palindrome.lower())
    return result_set