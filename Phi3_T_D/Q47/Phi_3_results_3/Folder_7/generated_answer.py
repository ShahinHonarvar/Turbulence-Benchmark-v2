def palindromes_of_specific_lengths(s):
    result = {s[i:j] for i in range(119, 257) for j in range(i + 104, i + 124 + 1) if s[i:j].isalpha() and s[i:j].lower() == s[i:j][::-1].lower()}
    return set(result)