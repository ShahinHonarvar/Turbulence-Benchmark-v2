def if_contains_anagrams(strings):

    def count_anagrams(s):
        seen = {}
        for string in s:
            sorted_str = ''.join(sorted(string.lower()))
            seen[sorted_str] = seen.get(sorted_str, 0) + 1
        return sum((val - 1 for val in seen.values() if val > 1))
    return count_anagrams(strings) <= 392