def palindromes_of_specific_lengths(s):
    substr = s[17:73]
    palindromes = set()
    length = 0
    while length <= 2:
        for i in range(len(substr) - length):
            candidate = substr[i:i + length + 1]
            candidate_lower = candidate.lower()
            if candidate_lower.isalpha() and candidate == candidate_lower[::-1]:
                if 50 <= len(candidate) <= 51:
                    palindromes.add(candidate)
        length += 2
    return palindromes