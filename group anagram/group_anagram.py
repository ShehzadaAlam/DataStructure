from collections import defaultdict


class GroupedAnagramSolution:
    def group_anagram(self, string_array):
        result = defaultdict(list)
        for word in string_array:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(word)
        return result.values()
