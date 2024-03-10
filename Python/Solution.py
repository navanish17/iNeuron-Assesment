# Question1






# Question2
def check(stalls, n, k, min_dist):
    count = 1
    last_position = stalls[0]
    
    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
    
    return count >= k

def largest_min_distance(stalls, n, k):
    stalls.sort()
    low = 1
    high = stalls[n-1] - stalls[0]
    
    while low < high:
        mid = (low + high + 1) // 2
        
        if check(stalls, n, k, mid):
            low = mid
        else:
            high = mid - 1
    
    return low

stalls = [1, 2, 4, 8, 9]
k = 3
n = len(stalls)

largest_min_dist = largest_min_distance(stalls, n, k)
print(largest_min_dist)

# Question3

def create_door_mat(N, M):
    pattern = [('.|.' * (2*i + 1)).center(M, '-') for i in range(N//2)]
    welcome_line = 'WELCOME'.center(M, '-')
    door_mat = pattern + [welcome_line] + pattern[::-1]
    
    for line in door_mat:
        print(line)


N = 7  # N is an odd natural number
M = 21  # M is 3 times N

create_door_mat(N, M)


# Question4

def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            left, right = j + 1, n - 1
            
            while left < right:
                total = sum([nums[i], nums[j], nums[left], nums[right]])
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left, right = left + 1, right - 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result


nums = [1, 0, -1, 0, -2, 2]
target = 0

result = fourSum(nums, target)
print(result)