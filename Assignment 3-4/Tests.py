from functions import *
def test_create_new_contestant():
    contestant=createContestantScore(7,8,10)
    assert(contestant[0]==7)
    assert(contestant[1]==8)
    assert(contestant[2]==10)
def test_add_new_contestant():
    list=[]
    add(list, 5, 6, 7)
    assert(list[0][0]==5)
    assert[list[0][1]==6]
    assert(list[0][2]==7)
def test_insert_new_contestant():
    list=[[1,2,3],[5,5,5]]
    insert(list,1,6,7,10)
    assert(list[1][0]==6)
    assert[list[1][1]==7]
    assert(list[1][2]==10)

def test_remove_scores():
    list=[[1,1,1],[2,5,7],[5,10,3]]
    remove(list,1,1)
    assert(list[1][0]==0)
    assert(list[1][1]==0)
    assert(list[1][2]==0)
def test_replace_scores():
    list=[[2,5,10],[3,4,9]]
    replace(list,1,3,5)
    assert(list[1][2]==5)
def test_list_sorted():
    list=[[1,3,5],[1,1,1],[6,6,6]]
    listSorted(list)
    assert(list[0]==[6,6,6])
    assert(list[1]==[1,3,5])
    assert(list[2]==[1,1,1])
def run_all_tests():
    test_create_new_contestant()
    test_add_new_contestant()
    test_insert_new_contestant()
    test_remove_scores()
    test_replace_scores()
    test_list_sorted()
    test_list_sorted()