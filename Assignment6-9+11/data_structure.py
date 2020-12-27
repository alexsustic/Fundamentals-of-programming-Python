import unittest
class DataStructure(object):

    def __init__(self):
        self._generalList = []
        self._index = -1

    def __iter__(self):
        "iterator for the class"
        return iter(self._generalList)

    def __next__(self):
        "verify is there exists a next element in the list and get it"
        if self._index > len(self._generalList) - 1:
            raise StopIteration
        else:
            self._index += 1
        return self._generalList[self._index]

    def __len__(self):
        "used to determine the lenght of a list"
        return len(self._generalList)

    def __setitem__(self, index, key):
        "set the value of a item with a new one"
        self._generalList[index] = key

    def __getitem__(self, index):
        "get the item from the position index"
        return self._generalList[index]

    def append(self, entity):
        self._generalList.append(entity)
        
    def remove(self, entity):
        self._generalList.remove(entity)

    def __delitem__(self, index):
        "deletes the item from position index from the list"
        del self._generalList[index]

    def pop(self, id):
        "pop the items from the list that have the same id"
        self._generalList.pop(id - 1)

    def clear(self):
        "clear the list"
        self._generalList.clear()

class Functions():
    
    def gnomeSort(self,list_to_sort,comparisonFunction):
        " If the index=0 than we increment the index"
        "We are always checking if list[index]>list[index-1] and if it's true than we swap the elements and decrement the index"
        "If it's false than we increment the index"
        "The moment the index gets to the len(list) position, the algortihm stops and return the sorted list"
        index = 0
        while index < len(list_to_sort):
            if index == 0 or comparisonFunction(list_to_sort[index], list_to_sort[index-1]) == True:
                index=index+1
            else:
                interchangeVariable = list_to_sort[index]
                list_to_sort[index] = list_to_sort[index-1]
                list_to_sort[index-1] = interchangeVariable
                index=index-1
                
        return list_to_sort
    


    def filter_list(self,list_to_be_filtered, filterCriteriaFunction):
        filtered_list = []
        for entity in list_to_be_filtered:
            if filterCriteriaFunction(entity) == True:
                filtered_list.append(entity)
        return filtered_list
    
class testDataStructure(unittest.TestCase):
    
    def setUp(self):
        self.dataStructure=DataStructure()
        
    def testAppend_newElement_ElementCorrectlyAdded(self):
        self.dataStructure.append('haha')
        self.assertEqual(self.dataStructure.__getitem__(0), 'haha')
        
    def testLength_list_correctLength(self):
        self.dataStructure.append('1')
        self.dataStructure.append('2')
        self.assertTrue(self.dataStructure.__len__()==2)
        
class testGnomeSort(unittest.TestCase):
    
    def setUp(self):
        self.mylist=[1,5,3,0,2,4]
        self.functions=Functions()
    def sort_function(self,number1,number2):
        return number1>=number2
        
    def testGnomeSort_MyList_SortedList(self):
        self.functions.gnomeSort(self.mylist, self.sort_function)
        self.assertEqual(self.mylist, [0,1,2,3,4,5])
        
class testFilter(unittest.TestCase):
    
    def setUp(self):
        self.mylist=[1,0,4]
        self.functions=Functions()
    def filter_function(self,number):
        return number!=0
    
    def testFilter_list_filteredList(self):
        newlist=self.functions.filter_list(self.mylist, self.filter_function)
        self.assertEqual(newlist, [1,4])
        
