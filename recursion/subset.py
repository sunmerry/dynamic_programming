import itertools
import collections
import time
import timeit
import os
class solution:
    def __init__(self, sets = {1,2,3}):
        self.set = list(sets)
        self.n = len(self.set)
        self.__subSet = list()
        self.subSetSums = list()
    def subsetSumRec(self,l = 0, ls = 0):
        if l == len(self.set):
            self.subSetSums.append(ls)
            return
        self.subsetSumRec(l+1,ls)
        self.subsetSumRec(l+1, ls + self.set[l])
    def getsubSet(self):
        return self.__subSet
    def subsetfun(self):
        for i in range(self.n+1):
            self.__subSet.extend(list(map(list,itertools.combinations(self.set, i))))
    def subsetSum(self):
        self.subSetSums = []
        for val in self.__subSet:
            self.subSetSums.append(sum(val))
    def getsubSetSum(self):
        return self.subSetSums


sets = solution()
start_time = time.time()
sets.subsetSumRec()
end_time = time.time()
elapsed_time = start_time - end_time
print("subsetSumRec",elapsed_time)


start_time = time.time()
sets.subsetfun()
sets.subsetSum()
end_time = time.time()
elapsed_time = start_time - end_time
print("subsetSum",elapsed_time)

print(timeit.Timer(sets.subsetSumRec).timeit())
print(timeit.Timer(sets.subsetfun).timeit())
print(timeit.Timer(sets.subsetSum).timeit())
#
# print("protected",sets.subSetSums)
# print("private via function",sets.getsubSet())
# print(collections.Counter(sets.subSetSums))
#
# s = { val : 0 for val in sets.subSetSums}
# print("s",s)
# for val in sets.subSetSums:
#     s[val] = s[val]+1
# print(s)
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# for folder,sub_folder,files in os.walk(os.getcwd()):
#     print(folder)
#     print(sub_folder)
#     print(files)
#
#
#
#
