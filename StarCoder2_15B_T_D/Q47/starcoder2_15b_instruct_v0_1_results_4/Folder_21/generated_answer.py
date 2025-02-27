def palindromes_of_specific_lengths(s):
    sub_string = s[100:296]
    palindromes = set()
    for length in range(136, 161):
        for i in range(len(sub_string) - length + 1):
            potential_palindrome = sub_string[i:i + length]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                palindromes.add(potential_palindrome)
    return palindromes