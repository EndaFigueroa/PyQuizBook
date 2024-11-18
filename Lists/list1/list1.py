from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    answer = []
    for i in t:
        answer.append(i)
    return answer
    
def drop_last(lst):
    answer = lst
    answer.pop()
    return answer
    


def drop_first_two(lst):
    return lst[2:]
    

def drop_mangle(lst):
    answer = lst[2:-1]
    return answer

def add_item_front(lst, a):
    answer = lst
    answer.insert(0,a)
    return answer

def add_item_end(lst, a):
    answer = lst
    answer.append(a)
    return answer

def add_list_to_list(lsta, lstb):
    answer = lsta + lstb
    return answer

def list_and_list_to_tuple(lsta, lstb):
    answer = (lsta,lstb)
    return answer
    # """
    # This function takes two lists and returns a tuple containing the two lists
    # """
    # pass # implement me

def list_and_list_to_list(lsta, lstb):
    answer = [lsta]+[lstb]
    return answer

def list_from_range(n):
    answer=[]
    for i in range(n):
        answer.append(i)
    return answer

def list_from_range2(n, m):
    answer = []
    for i in range (n,m):
        answer.append(i)
    return answer

def list_from_range3(n, m):
    answer = []
    for i in range (n,m+1):
        answer.append(i)
    return answer
    # """
    # This function returns list with n..m (including m(!)) as integers in a list
    # """
    # pass # implement me

def list_from_range4(n, m):
    answer = []
    for i in range(n+1,m+1):
        answer.append(i)
    return answer
    # """
    # This function returns list with n..m (WITHOUT n and including m) as integers in a list
    # """
    # pass # implement me

def list_from_range_by(n, step):
    answer = []
    for i in range (0,n,step):
        answer.append(i)
    return answer

def rev_list(lst):
    answer = lst
    answer.reverse()
    return answer
    # """
    # This function returns list which is a reverse of the argument list
    # (read the test)
    # """
    # pass # implement me

def concat_list_indexwise(lst1, lst2):
    answer = [x+y for x,y in zip(lst1,lst2)]
    return answer

def square_each_item(lst):
    return [x**2 for x in lst]
    # """
    # This function returns list which each item in argument list has been squared
    # (read the test)
    # """
    # pass # implement me

def remove_empty_strs(lst):
    answer = []
    for i in lst:
        if (i is not ""):
            answer.append(i)
    return answer

def remove_item_from(lst, aaa):
    answer = []
    for i in lst:
        if (i is not aaa):
            answer.append(i)
    return answer

def leave_item_in(lst, aaa):
    answer = []
    for i in lst:
        if (i == aaa):
            answer.append(i)
    return answer

def length_of(lst):
    return len(lst)