# ID успешной посылки 50393600
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    q = nums[len(nums) // 2]
    s_nums = []
    m_nums = []
    e_nums = []

    for n in nums:
        if n[1] > q[1]:
            s_nums.append(n)
        elif n[1] < q[1]:
            m_nums.append(n)
        else:
            if n[0] == q[0]:
                e_nums.append(n)
            elif n[2] != q[2]:
                s_nums.append(n) if n[2] < q[2] else m_nums.append(n)
            else:
                s_nums.append(n) if n[0] < q[0] else m_nums.append(n)

    return quicksort(s_nums) + e_nums + quicksort(m_nums)


def main():
    n = int(input())
    p = []
    for i in range(n):
        q = list(input().split())
        q[1] = int(q[1])
        q[2] = int(q[2])
        p.append(q)
    sort = quicksort(p)
    for s in sort:
        print(s[0])


if __name__ == '__main__':
    main()
