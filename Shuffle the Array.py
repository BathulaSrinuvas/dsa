class SolutionShuffleArray():
    def shuffle(nums: list[int], n: int) -> list[int]:
        output = []
        x = nums[0:n]
        y = nums[n:]
        for i in range(n):
            output.append(x[i])
            output.append(y[i])
        return output
        # for index, i in enumerate(nums):

        #     for j in range(i+1,nums):
        #         return i,j

nums = [2,5,1,3,4,7] 
n = 3
