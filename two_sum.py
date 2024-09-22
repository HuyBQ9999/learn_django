class Solution:
    def two_sum_all_cases(self, nums, target):
        index_map = {}
        result = []  
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in index_map:
                result.append([index_map[complement], i])
            index_map[num] = i
        return result
    
if __name__ == "__main__":
    func = Solution()
    result = func.two_sum_all_cases([1,4,5,2,3,6], 7)
    print(result)