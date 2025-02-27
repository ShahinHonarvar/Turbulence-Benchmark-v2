from collections import defaultdict

def if_contains_anagrams(strings):
    char_count_map = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            s_lower = s.lower()
            count_chars = [0] * 26
            for char in s_lower:
                if char.isalpha():
                    count_chars[ord(char) - ord('a')] += 1
            char_count_map[tuple(count_chars)] += 1
    anagram_pairs = 0
    for count in char_count_map.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 40