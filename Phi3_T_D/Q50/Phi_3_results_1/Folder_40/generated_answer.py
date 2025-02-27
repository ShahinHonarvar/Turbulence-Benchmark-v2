def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    words_processed = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                if (words[i], words[j]) not in words_processed:
                    anagram_count += 1
                    words_processed.add((words[i], words[j]))
                    if anagram_count >= 3:
                        return True
    return False