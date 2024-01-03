def largestNumber(nums) -> str:
    out = ""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (str(nums[j])[0] > str(nums[i])[0]):
                nums[i], nums[j] = nums[j], nums[i]
            if len(str(nums[i])) > 1:
                if (str(nums[j])[1: ]) > (str(nums[i])[1: ]):
                    nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    for k in nums:
        out += str(k)
    return (out)

nums = [111311, 1113]
print(largestNumber(nums))


