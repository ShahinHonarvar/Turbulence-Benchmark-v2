def palindromes_of_specific_lengths(string):
    palindromes = set()
    lower_case_string = string.lower()
    substring = lower_case_string[103:277]
    for length in range(100, 170):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes