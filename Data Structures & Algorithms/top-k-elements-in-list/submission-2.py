class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        
        bucket = [[] for i in range(len(nums))]
        for key, value in count.items():
            print(key, value)
            bucket[value-1].append(key)

        count_k = 0
        top_k = []
        for i in range(len(nums)-1, -1, -1):
            if bucket[i]:
                for item in bucket[i]:
                    top_k.append(item)
                    count_k += 1
                    print(count_k)
                    if count_k == k: return top_k
                