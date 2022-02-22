"""
【GC】https://www.jianshu.com/p/12544c0ad5c1
引用计数、标记（清除/整理）、分代
三色标记法：初始全都未访问（白） -> 引用对象「未」完全访问（灰） -> 引用对象「已」完全访问（黑）
读写屏障：解决漏标（a->b->c），b->c断开，a->c建立，因为a已经是黑色，所以会忽略掉c（应该标记为灰色）

kafka 存储结构：
Broker、Topic、Partition、Segment、offset

mysql：
redo：按block写，
redo：ROLLBACK、mvcc
隔离级别：
    read uncommited：脏读、幻读、不可重复读
    READ commited：幻读、不可重复读
    repeatable read：幻读
    serializable：无
分布式事务：xa，tcc

http：
500 internal server error
501 not implemented,
502 bad gateway 网关访问得到无效的响应
503 service unavaliable 服务暂不可用
504 gateway timeout 网关访问超时
"""

def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:  # <= 就是 upper_bound
            l = m + 1
        else:
            r = m
    return l


"""旋转数组最小值"""
def minArray(self, nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m 
        else:
            r -= 1
    return nums[l]


def quick_sort(nums):    
    """快速排序"""
    if len(nums) < 2:  # 递归入口及出口        
        return nums

    left, mid, right = [], [], []
    pivot = nums[0]
    for n in nums:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            mid.append(n)
    return quick_sort(left) + mid + quick_sort(right)
