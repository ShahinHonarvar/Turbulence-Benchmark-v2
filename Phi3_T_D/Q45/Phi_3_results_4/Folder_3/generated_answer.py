def palindromes_between_indices(s: str):
    target_chars = s[6:10].lower()
    letter_counts = {}
    for char in target_chars:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    palindromes = set()
    for _, count in letter_counts.items():
        if count >= 3:
            center = ''.join([char * (count // 2) for char in letter_counts if count // 2 > 0])
            letters = ''.join([char * (count % 2) for char in letter_counts if count % 2 > 0])
            palindromes.add(center + letters + center[::-1])
    return palindromes