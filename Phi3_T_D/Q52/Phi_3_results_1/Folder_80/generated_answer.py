def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 275):
        potential_palindrome = s[i:i + 276]
        if potential_palindrome == potential_palindrome[::-1]:
            result_set.add(potential_palindrome)
    return result_set