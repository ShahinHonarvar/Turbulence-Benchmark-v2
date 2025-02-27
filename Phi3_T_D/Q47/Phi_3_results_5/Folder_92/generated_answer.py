def palindromes_of_specific_lengths(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[:5].lower()
    palindromes = set()
    for length in range(inclusive_range(3, 4)):
        for index in range(len(substring) - length + 1):
            candidate = substring[index:index + length]
            if candidate.isalpha() and set(candidate) <= alphabet and (candidate == candidate[::-1]):
                palindromes.add(candidate)
    return palindromes

def inclusive_range(start, end):
    return range(start, end + 1)