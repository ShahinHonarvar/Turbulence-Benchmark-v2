from collections import Counter

def palindromes_between_indices(s):
    substring = s[0:5]
    char_count = Counter(substring.lower())
    odd_counts = [char for char, count in char_count.items() if count % 2 != 0]
    palindromes = set()
    if len(odd_counts) > 1:
        return set()

    def generate_palindromes(half, full_char_count):
        if sum(full_char_count.values()) == 0:
            palindromes.add(half + half[::-1])
            return
        for char in full_char_count.copy():
            if full_char_count[char] > 1:
                full_char_count[char] -= 2
                generate_palindromes(half + char, full_char_count)
                full_char_count[char] += 2
    if len(odd_counts) == 1:
        middle_char = odd_counts[0]
        char_count[middle_char] -= 1
        generate_palindromes(middle_char, char_count)
    else:
        generate_palindromes('', char_count)
    return set(filter(lambda x: len(x) >= 4, palindromes))