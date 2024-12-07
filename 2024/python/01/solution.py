from collections import Counter

list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        nums = [int(s) for s in line.split()]
        list1.append(nums[0])
        list2.append(nums[1])

list1.sort()
list2.sort()
n = len(list1)

print(sum(abs(list1[i] - list2[i]) for i in range(n)))

counts = Counter(list2)
print(sum(n * counts[n] for n in list1))


