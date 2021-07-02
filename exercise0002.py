import pymysql,random,string

forchoice = string.ascii_letters + "0123456789"


def generate(num, lenth):
    list_code = set()

    while len(list_code) < num:
        Re = ""
        for y in range(lenth):
            Re += random.choice(forchoice)
        list_code.add(Re)
    return list_code

generate(200,20)
def storemysql(list_code):
    conn = pymysql.connect(
        host ='rm-wz9d4iopy2m6549id8o.mysql.rds.aliyuncs.com',
        port =3306,
        user ='qimu_0527',
        passwd = 'qimu_0527',
        db = 'exercise0002'
    )

    cur = conn.cursor()
   
    cur.execute("drop table if exists user")
    cur.execute('''create table if not exists user(
                            id int not null auto_increment,
                            code varchar(32) not null,
                            primary key(id)
                        )''') 
    for code in list_code:
        cur.execute('insert into user(code) values(%s)',(code))
        cur.connection.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    storemysql(generate(200,20))
    print('OK')

