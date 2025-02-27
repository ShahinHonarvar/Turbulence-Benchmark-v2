def palindrome_of_length_n(s):
    n = 60
    set_of_palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - n + 1):
        sub = s_lower[i:i + n]
        if sub == sub[::-1]:
            set_of_palindromes.add(sub)
    return set_of_palindromes