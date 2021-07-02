import random,string

forchoice = string.ascii_letters + "0123456789"

def generate(num, lenth):
    list_code = set()

    while len(list_code) < num:
        Re = ""
        for y in range(lenth):
            Re += random.choice(forchoice)
        list_code.add(Re)
        
    for i in list_code:
        print(i)
    return list_code
if __name__ == '__main__':
    generate(200, 20)
    