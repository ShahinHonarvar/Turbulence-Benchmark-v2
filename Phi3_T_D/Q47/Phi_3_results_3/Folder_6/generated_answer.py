from itertools import product

def palindromes_of_specific_lengths(s):
    filtered_substr = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for start in range(len(filtered_substr) - length + 1):
            candidate = filtered_substr[start:start + length]
            if all((c.isalpha() for c in candidate.lower())) and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes