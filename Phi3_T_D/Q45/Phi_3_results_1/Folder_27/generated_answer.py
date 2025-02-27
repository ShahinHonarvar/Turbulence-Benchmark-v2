def palindromes_between_indices(s):
    substring = s[2:9]
    possible_chars = ''.join(sorted(set(substring.lower())))
    palindromes = {''.join(palindrome) for palindrome in itertools.permutations(possible_chars, 6)}
    return {p for p in palindromes if p.lower() == p[::-1]}