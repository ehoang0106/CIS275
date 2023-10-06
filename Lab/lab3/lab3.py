def reverse(lst):

    left = 0
    right = len(lst) - 1


    while left < right:
        #swap
        lst[left], lst[right] = lst[right], lst[left]

        #move toward
        left +=1
        right -=1

    return lst


print(reverse([1,2,3,4]))
print(reverse([5,4,3,2,1]))

"""
The function uses a two-pointer approach to reverse the element in the list. Each element will be involed in a swap operation once
This will give the function a linear time complexity of O(n).
Because the O(n) time complexity is that the two pointers are moving towards each other, and the loop runs roughly n/2 times.
Each iteration of the loop performs a constant amount of work. Then the time complexity is O(n/2), which is equivalent to O(n)
"""