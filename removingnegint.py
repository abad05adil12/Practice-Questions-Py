def num(nums):
    result=[]
    for num in nums:
        if num>=0:
            result.append(num)
            result.sort()
    return result

print(num([-1,2,43,-4,15,-6,7,-8,90,-10]))