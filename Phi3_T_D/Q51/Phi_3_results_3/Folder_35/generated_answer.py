def if_contains_anagrams(lst):

    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1.lower()) == sorted(word2.lower())

    def count_anagrams(lst):
        count = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    count += 1
        return count
    return count_anagrams(lst) <= 210