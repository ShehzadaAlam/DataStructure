class TopkElement:
    def top_k_elements(self, list_arr, k):
        count_list = [[] for i in range(len(list_arr) + 1)]
        count = {}
        res = []

        for i in range(len(list_arr)):
            count[i] = 1 + count.get(i, 0)

        for n, c in count.items():
            count_list[c].append(n)

        for elem_list in range(len(count_list) - 1, 0, -1):
            for elem in elem_list:
                res.append(elem)
                if len(res) == k:
                    return res
