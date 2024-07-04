a = [1, 2, 3]
print(a[1])

# 수열 만들기
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))
print(list(range(1,10,2)))

# 다음 리스트의 평균을 출력하라.
nums = list(range(1,6))
eva = (nums[0] + nums[1] + nums[2] + nums[3] + nums[4]) / len(nums)
print(eva)

# 리스트에 요소 추가하기
num_list = list(range(1,6))
num_list.append(6)
print(num_list)
num_list.remove(3)
print(num_list)
