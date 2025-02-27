def find_palindromes(s, start, end):
    palindromes = set()
    for i in range(start, min(end + 1, len(s))):
        for j in range(i + 29, min(end + 1, i + 32 + 1)):
            segment = s[i:j + 1]
            if segment.isalpha() and segment.lower() == segment[::-1].lower():
                palindromes.add(segment.lower())
    return palindromes

def palindromes_of_specific_lengths(s):
    return find_palindromes(s, 23, 82)