def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    sub_string = s[11:94]
    selected_palindromes = set()
    lower_bound, upper_bound = (34, 54)
    for length in range(lower_bound, upper_bound + 1):
        for i in range(len(sub_string) - length + 1):
            candidate = sub_string[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                selected_palindromes.add(candidate)
    return selected_palindromes