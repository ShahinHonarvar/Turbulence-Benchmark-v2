def if_contains_anagrams(lst):

    def are_anagrams(str1, str2):
        counts = {}
        for char in str1.lower():
            if char.isalpha() and char not in counts:
                counts[char] = 1
            elif char.isalpha():
                counts[char] += 1
        for char in str2.lower():
            if char.isalpha() and char in counts:
                counts[char] -= 1
            elif char.isalpha():
                return False
        return all((value == 0 for value in counts.values())) and sum(counts.values()) >= 3 * 2
    unique_anagrams = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                unique_anagrams.add(tuple(sorted(lst[i].lower())))
                unique_anagrams.add(tuple(sorted(lst[j].lower())))
    return len(unique_anagrams) <= 255