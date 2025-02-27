from collections import Counter

def palindromes_between_indices(s):
    s = s[:7].lower()
    counter = Counter(s)
    single_chars = [char for char, count in counter.items() if count % 2 == 1]
    half_palindrome = ''.join([char * (count // 2) for char, count in counter.items()])
    if len(single_chars) > 1:
        return set()

    def generate_palindromes(half, single):
        if not half:
            return {single}
        palindromes = set()
        for i in range(len(half)):
            new_half = half[:i] + half[i + 1:]
            for p in generate_palindromes(new_half, single):
                palindromes.add(half[i] + p + half[i])
        return palindromes
    palindromes = generate_palindromes(half_palindrome, single_chars[0] if single_chars else '')
    return {p for p in palindromes if len(p) >= 3}