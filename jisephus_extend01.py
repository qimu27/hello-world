class People():

    def __init__(self,name,id,gender):
        self.name = name
        self.id = id
        self.gender = gender

qwe= People('qwe','01','男')
qw= People('qw','02','男')
asd= People('asd','03','男')
zxc= People('zxc','04','男')
ert= People('ert','05','男')
rty= People('rty','06','男')
yui= People('yui','07','男')
iop= People('iop','08','男')

start_people = [qwe,qw,asd,zxc,ert,rty,yui,iop]

def josephus_poblem(start_people,k):   #命名修改：N 改为num。   k 改为 step,inter
    finally_people = start_people
    
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
        
        if remainder > 0:
            for i in range(remainder):        
                finally_people.insert(0,finally_people[len(finally_people)-1])          
                finally_people.pop()
            print(finally_people) 

    # 由题意知：当剩下的人小于 k 时,迭代最终剩下 1 个人
    while 1 < len(finally_people) <= k-1:
        remainder = k%len(finally_people)
        finally_people.pop(remainder-1)
    
    print(finally_people[0].name)

josephus_poblem(start_people,3) 
    

