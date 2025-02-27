from itertools import permutations

def palindromes_between_indices(text):
    start, end = (7, 9)
    letters = text[start:end + 1].lower()
    char_counts = {}
    for char in letters:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    even_chars = ''.join([char * (count // 2) for char, count in char_counts.items() if count % 2 == 0])
    single_odd_char = [char for char, count in char_counts.items() if count % 2 == 1]
    palindromes_set = set()
    if not single_odd_char:
        for p in permutations(even_chars, len(even_chars) + 1):
            palindromes_set.add(''.join(p) + ''.join(p[::-1]))
    else:
        base = ''.join(even_chars)
        for permutation in permutations(base, len(base)):
            central_char = single_odd_char[0]
            for i in range(len(permutation) + 1):
                palindrome_candidate = permutation[:i] + central_char + permutation[i:]
                palindrome_candidate += palindrome_candidate[-2::-1]
                if len(palindrome_candidate) >= 3:
                    palindromes_set.add(palindrome_candidate)
    return {p for p in palindromes_set if len(p) >= 3}