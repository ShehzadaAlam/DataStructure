from collections import Counter


class AnagramSolution:
    @classmethod
    def anagram_solution(self, source, target):
        # # Solution 3
        # sorted(source) == sorted(target)

        # # Solution 2
        # Counter(source) == Counter(target)

        # Solution 1
        if len(source) != len(target):
            return False

        source_hash_map = {}
        target_hash_map = {}

        for i in range(len(source)):
            source_hash_map[source[i]] = 1 + source_hash_map.get(source[i], 0)
            target_hash_map[target[i]] = 1 + target_hash_map.get(target[i], 0)
        for c in source_hash_map:
            if source_hash_map[c] != target_hash_map.get(c, 0):
                return False
        return True
