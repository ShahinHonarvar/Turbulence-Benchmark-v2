def palindromes_between_indices(s):
    substring = s[1:4].lower()
    possible_chars = set(substring)
    all_palindromes = set()
    for a in possible_chars:
        for b in possible_chars:
            palindrome = a + b + b + a
            if palindrome[0] == palindrome[-1] and palindrome[1] == palindrome[-2]:
                all_palindromes.add(palindrome)
    return all_palindromes