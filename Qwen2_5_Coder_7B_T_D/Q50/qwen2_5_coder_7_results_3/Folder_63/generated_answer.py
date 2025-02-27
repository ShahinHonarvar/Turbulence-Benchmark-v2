from collections import Counter

def if_contains_anagrams(words):

    def count_anagrams(words):
        anagram_count = 0
        for word in words:
            if len(word) >= 3:
                sorted_word = ''.join(sorted(word.lower()))
                counter = Counter(sorted_word)
                anagram_count += counter['a'] * counter['n'] * counter['g'] * (counter['a'] - 1) * (counter['n'] - 1) * (counter['g'] - 1) // 6
        return anagram_count
    return count_anagrams(words) >= 89