def TwoSum(nums: list,target: int):
    positions = []
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)-1):
            if nums[i] + nums[j] == target:
                positions.append(i)
                positions.append(j)
                print(positions)
                return positions



numeros = [2,7,11,15]
alvo = 9
TwoSum(numeros, alvo)