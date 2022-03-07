from streaming_median import MedianFinder

# [2,4,6,8,9,11]

med = MedianFinder()
med.add_num(4)
med.add_num(2)
med.add_num(6)
med.add_num(11)
med.add_num(8)
med.add_num(9)
# med.add_num(55)

res = med.find_median()
print(res)
