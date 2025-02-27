def if_contains_anagrams(strings):

    def count_anagrams():
        anag_count = 0
        for i in range(len(strings)):
            hash_set = set()
            for other in range(i + 1, len(strings)):
                if sorted(strings[i].lower()) == sorted(strings[other].lower()):
                    anag_count += 1
                    break
        return anag_count
    return count_anagrams() <= 67