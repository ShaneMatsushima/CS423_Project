LIST = []

def edit(i):
    global LIST
    LIST.append(i)


def printLIST():
    global LIST
    print(LIST)
edit(1)
edit(1)
edit(1)
edit(1)
edit(1)

printLIST()