def allArrayMethods(nums: list[int]):
    print("Orignal List : " , nums)
    nums.append(6)
    print("After appending 6", nums)
    nums.pop()
    print("After using pop ", nums )
    nums.reverse()
    print("After using reverse", nums)
    nums.sort()
    print("After using sort ", nums)
    print("Using Count on 4 -  ", nums.count(4))
    nums.clear()
    print("After using clear", nums)

nums  = [1,2,4,4,14,3,4,7,1,12]
allArrayMethods(nums)