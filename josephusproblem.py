# 约瑟夫环问题
# 假设存在 N 个人围成一圈，编号分别为1,2,3，--，N
# 从1开始数，每数到 k 则，数到 k 的人淘汰,
# 问剩下的人的编号为多少？

def josephus_problem(N,k):#命名修改：N 改为num。   k 改为 step,inter
    start_people = list(range(1,N+1))
    finally_people = start_people.copy()
    print(finally_people)
    # 当 N >= k 时,迭代剩下 k-1 个人 
    while len(finally_people) > k-1:
        quotient,remainder = divmod(len(finally_people),k)
        delete_index = []
        null_list = []
        
        for i in range(1,quotient+1):
            delete_index.append(k*i-1) # 需要同时删除的元素索引列表
        for i in range(len(finally_people)):
            if i not in delete_index:
                null_list.append(finally_people[i])
        finally_people = null_list
        print(finally_people)
        if remainder > 0:
            for i in range(remainder):        
                finally_people.insert(0,finally_people[len(finally_people)-1])          
                finally_people.pop()
            print(finally_people)     
    # 由题意知：当剩下的人小于 k 时,迭代最终剩下 1 个人
    while 1 < len(finally_people) <= k-1:
        remainder = k%len(finally_people)
        finally_people.pop(remainder-1)
    
        print(finally_people[0])
        
if __name__ == "__main__":
    josephus_problem(7,3)