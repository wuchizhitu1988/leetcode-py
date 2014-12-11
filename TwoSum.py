class Solution:
    def twoSum(self, num, target):
        if not sum:
            return -1, -1
        record = {}
        for idx, value in enumerate(num):
            if target - value in record:
                return record[target - value] + 1, idx + 1
            record[value] = idx
            
        return -1, -1
