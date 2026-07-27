def rotate(nums,k):
    for i in range(k):
        last = nums[-1]
        nums.pop()
        nums.insert(0, last)
        print(str(i + 1) + " rotate: " + str(nums))

rotate([1,2,3,4,5,6,7],5)    