#!/user/bin/python
#filename:odbchelper.py

def buildConnectionString(params):
    '''Build a connection string froom a dictionary of parameters.
    Return string.'''
    return ":".join(["%s=%s" %(k, v) for k, v in params.items()])

def fib(n):
    print("n = ", n)
    if n > 1:
        return n * fib(n -1)
    else:
        print("end of the line!")
        return 1

if __name__ == "__main__":
    myParams = {"server":"mpilgrim",
                "database":"master",
                "uid":"sa",
                "pwd":"secret"}
    print(buildConnectionString(myParams))
    print("fib(5) = ", fib(5))