from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    counts = Counter(substring)
    middle = [char for char, count in counts.items() if count % 2]
    even_counts = {char: count // 2 for char, count in counts.items() if count % 2 == 0}
    if len(middle) > 1:
        return set()
    results = set()

    def backtrack(path, remaining):
        if not remaining:
            palindrome = path + middle[0] + path[::-1] if middle else path + path[::-1]
            if len(palindrome) >= 5:
                results.add(palindrome)
            return
        for char in list(remaining):
            if remaining[char] > 1:
                remaining[char] -= 2
                backtrack(path + char, remaining)
                remaining[char] += 2
    backtrack('', dict(even_counts))
    return results