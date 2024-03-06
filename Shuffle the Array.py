class SolutionShuffleArray():
    def shuffle(nums: list[int], n: int) -> list[int]:
        output = []
        x = nums[0:n]
        y = nums[n:]
        for i in range(n):
            output.append(x[i])
            output.append(y[i])
        return output
nums = [2,5,1,3,4,7] 
n = 3
