from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    anagram_counts = Counter(anagram_dict)
    total_anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return total_anagram_pairs >= 68