from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:7]
    counter = Counter(substring.lower())
    single_chars = [char for char, freq in counter.items() if freq % 2 != 0]
    half_palindrome = ''.join([char * (freq // 2) for char, freq in counter.items()])

    def generate_palindromes(half, singles):
        if len(singles) == 0:
            return {half + half[::-1]}
        result = set()
        for i in range(len(singles)):
            mid = singles[i]
            new_singles = singles[:i] + singles[i + 1:]
            for p in generate_palindromes(half, new_singles):
                result.add(mid.join([half, half[::-1]]))
        return result
    palindromes = generate_palindromes(half_palindrome, single_chars)
    return {p for p in palindromes if len(p) >= 3}