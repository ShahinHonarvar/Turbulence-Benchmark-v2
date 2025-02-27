def get_subpalindromes(s, start, end):
    prefixes = set()
    palindromes = set()
    unique_chars = set(s.lower()[start:end + 1])
    for char in unique_chars:
        for p in prefixes:
            if len(char + p) >= 4 and char + p == (char + p)[::-1]:
                palindromes.add(char + p)
            if len(p + char) >= 4 and p + char == (p + char)[::-1]:
                palindromes.add(p + char)
        prefixes.add(char)
        for pc in prefixes:
            if len(char + pc) >= 4 and char + pc == (char + pc)[::-1]:
                palindromes.add(char + pc)
            if len(pc + char) >= 4 and pc + char == (pc + char)[::-1]:
                palindromes.add(pc + char)
    return palindromes

def palindromes_between_indices(s):
    return get_subpalindromes(s, 3, 5)