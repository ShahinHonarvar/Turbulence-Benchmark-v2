def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    count = 0
    seen_words = set()
    for word1 in words:
        if len(word1) < 3:
            continue
        for word2 in seen_words:
            if is_anagram(word1, word2):
                count += 1
                break
        if count >= 40:
            return True
        seen_words.add(word1.lower())
    return False