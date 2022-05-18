import bisect

def MovingMedian(nums):
  k = nums[0]
  nums = nums[1:]
  print(k)
  print(k//2)
  print(nums)

  if k == 0: return []
  length = len(nums)
  
  if k > length:
    k = length
  ans = []

  sum = 0
  for i in range(1, k):
    sum = sum + nums[i - 1]
    ans.append(str(int(sum / i)))
    print('sum: ',sum)
    print('ans: ', ans)

  window = sorted(nums[0:k])
  
  for i in range(k, length + 1):
    print('window: ', window)
    print(window[k//2])
    print(window[(k-1) // 2])
    
    ans.append(str(int((window[k // 2] + window[(k - 1) // 2]) / 2.0)))
    if i == length: break
    index = bisect.bisect_left(window, nums[i - k])
    window.pop(index)
    bisect.insort_left(window, nums[i])
  res = ','
  return res.join(ans)

# keep this function call here
#print(MovingMedian([5,2,4,6,12,45,10,2]))
#print(MovingMedian([3, 0, 0, -2, 0, 2, 0, -2]))


def ArrayChallenge(arr):

  # code goes here
  slide_size = arr[0]
  arr = arr[1:]
  output = []
  lenarr = len(arr)

  if slide_size > lenarr: 
    slide_size = lenarr

  total = 0
  for i in range(1, slide_size):
    total = total + arr[i - 1]
    output.append(str(int(total / i)))

  window = sorted(arr[0:slide_size])
  for i in range(1, lenarr + 1 - (slide_size - 1)):
    output.append(str(int((window[slide_size // 2] + window[(slide_size-1) // 2]) / 2)))
    window = sorted(arr[i: slide_size + i])
    
  return ','.join(output)

print(ArrayChallenge([5,2,4,6])
