strarray = [3, 6, 7, 9, 23, 67, 10]
target = 16


def find_sum(strarray, target):
    prev = {}
    for index, value in enumerate(strarray):
        diff = target - value
        if diff in prev:
            return [prev[diff], index]
        prev[value] = index
    return


print(find_sum(strarray, target))
print("-------")

