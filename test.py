
def productExceptSelf(nums) :
    size = len(nums)
    if size >= 2 and size <= (10 ** 5):
        left_products = [1] * size
        product = 1
        for i in range(1, size):
            product *= nums[i - 1]
            left_products[i] = product
        right_product = 1
        for i in range(size - 1, -1, -1):
            left_products[i] *= right_product
            right_product *= nums[i]
        return left_products
    else:
        return []

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))



