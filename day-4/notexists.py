def myfile():
    try:
        d=open('D:\SreenuS\pythonProject1','srinu')
        print(d.read())
    except(FileNotFoundError):
        return('not exists')
emp=myfile()
print(emp)