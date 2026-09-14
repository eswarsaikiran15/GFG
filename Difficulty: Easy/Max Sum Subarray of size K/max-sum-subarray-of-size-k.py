class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n=len(arr)
        window_sum=sum(arr[:k])
        max_sum=window_sum
        
        left=0
        for right in range(k,n):
            window_sum-=arr[left]
            window_sum+=arr[right]
            
            left+=1
            
            max_sum= max(max_sum,window_sum)
        return max_sum