def if_contains_anagrams(words):

    def normalize(word):
        return sorted(word.lower())

    def has_anagrams(word_list):
        anagram_buckets = {}
        for word in word_list:
            nword = normalize(word)
            if nword in anagram_buckets:
                anagram_buckets[nword].append(word)
            else:
                anagram_buckets[nword] = [word]
        pairs = 0
        for anagrams in anagram_buckets.values():
            if len(anagrams) > 1:
                pairs += len(anagrams) * (len(anagrams) - 1) // 2
        return pairs
    return has_anagrams(words) >= 92