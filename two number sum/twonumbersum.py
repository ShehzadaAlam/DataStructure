class TwoNumSolution:
    @classmethod
    def two_num_sum(self, int_array, target):
        prev_hash = {}
        for idx, num in enumerate(int_array):
            diff = target - num
            if diff in prev_hash:
                return [prev_hash[diff], idx]
            prev_hash[num] = idx
        return
