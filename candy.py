def canPlaceFlowers(flowerbed, n: int) -> bool:
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                count += 1
                i += 2
            else:
                i += 3
        else:
            i += 2
    return count >= n

flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))