class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #counts the occurences of each value
        freq = [[] for i in range(len(nums) + 1)] #array the same size as input array

        for num in nums: 
            count[num] = 1 + count.get(num, 0) #how many times a certain number occurs, increment
        for num, c in count.items(): #go through each value that we counted, USE ITEMS, RETURNS EACH KEY VALUE PAIR
            freq[c].append(num) #for every num in count, want to insert into freq array at index count, the value n.
            #this value num occurs c # of times

        res = []
        for i in range(len(freq) - 1, 0, -1): #iterate through the array freq in discending order
            for n in freq[i]: #the value at given index, index is # of times a value appears
                res.append(n)
                if len(res) == k: #once the length of our result is = to k, return results
                    return res
