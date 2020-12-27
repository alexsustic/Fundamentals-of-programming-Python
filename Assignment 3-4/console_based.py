from functions import *
from Tests import *
import copy
def ui_add(list,command_list,undo_List):
    if (len(command_list) != 4):
        raise Exception("Invalid syntax!")
    else:
        score1=int(command_list[1])
        score2 = int(command_list[2])
        score3 = int(command_list[3])
        if (score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10 or score3 < 0 or score3 > 10):
            raise Exception("Invalid score!")
        else:
         add(list,score1,score2,score3)
         undo_List.append(copy.deepcopy(list))


def ui_insert(list,command_list,undo_List):
    if (len(command_list) != 6):
        raise Exception("Invalid syntax!")
    else:
        position=int(command_list[5])
        score1=int(command_list[1])
        score2 = int(command_list[2])
        score3= int(command_list[3])
        if(command_list[4]!="at"):
            raise Exception("Invalid syntax!")
        elif(score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10 or score3 < 0 or score3 > 10 ):
            raise Exception("Invalid score!")
        elif(position<0 or position>len(list)-1):
            raise Exception("Position out of range!")
        else:
            insert(list,position,score1,score2,score3)
            undo_List.append(copy.deepcopy(list))

def ui_remove(list,command_list,undo_List):
     if(len(command_list)==2):
         position=int(command_list[1])
         if(position<0 or position>len(list)-1):
             raise Exception("Inexistent contestant")
         else:
           remove(list,position,position)
           undo_List.append(copy.deepcopy(list))
     elif(len(command_list)==4):
         startPosition=int(command_list[1])
         finalPosition=int(command_list[3])
         if(command_list[2]!="to"):
             raise Exception("Invalid syntax")
         elif (startPosition < 0 or startPosition> len(list) - 1 or finalPosition<0 or finalPosition>len(list)-1):
             raise Exception("Inexistent contestant")
         else:
           remove(list,startPosition,finalPosition)
           undo_List.append(copy.deepcopy(list))
     elif(len(command_list)==3 and command_list[1]=="<"):
         if(int(command_list[2])<0):
             raise Exception("Invalid term of comparation!")
         else:
           number=int(command_list[2])
           removeLessThanANumber(list,number)
           undo_List.append(copy.deepcopy(list))

     elif (len(command_list) == 3 and command_list[1] == "="):
         if (int(command_list[2]) < 0):
             raise Exception("Invalid term of comparation!")
         else:
           number = int(command_list[2])
           removeEqualToANumber(list, number)
           undo_List.append(copy.deepcopy(list))

     elif (len(command_list) == 3 and command_list[1] == ">"):
         if (int(command_list[2]) < 0):
             raise Exception("Invalid term of comparation!")
         else:
           number = int(command_list[2])
           removeGreaterThanANumber(list, number)
           undo_List.append(copy.deepcopy(list))
     else:
         raise Exception("Invalid syntax")
def ui_replace(list,command_list,undo_List):
    if (len(command_list) != 5):
        raise Exception("Invalid syntax!")
    else:
        position = int(command_list[1])
        problem = int(command_list[2])
        newScore = int(command_list[4])
        if(command_list[3]!="with"):
            raise Exception("Invalid syntax!")
        elif(problem<1 or problem>3):
            raise Exception("Inexistent probe!")
        elif(position<0 or position>len(list)-1):
            raise Exception("Inexistant contestant")
        elif(newScore<0 or newScore>10):
            raise Exception("Invalid score!")
        else:
           replace(list,position,problem,newScore)
           undo_List.append(copy.deepcopy(list))
def ui_avg(list,command_list,undo_List):
    if (len(command_list) != 4):
        raise Exception("Invalid syntax!")
    else:
       startPosition = int(command_list[1])
       lastPosition = int(command_list[3])
       if(command_list[2]!="to"):
           raise Exception("Invalid syntax!")
       elif(startPosition<0 or startPosition>len(list)-1 or lastPosition<0 or lastPosition>len(list)-1) :
           raise Exception("Inexistent contestant")
       else:
            print(averageOfAverageListScore(list,startPosition,lastPosition))
def ui_min(list,command_list,undo_List):
      if (len(command_list) != 4):
          raise Exception("Invalid syntax!")
      else:
        startPosition = int(command_list[1])
        finalPosition = int(command_list[3])
        if (command_list[2] != "to"):
          raise Exception("Invalid syntax!")
        elif (startPosition < 0 or startPosition> len(list) - 1 or finalPosition< 0 or finalPosition > len(list) - 1):
          raise Exception("Inexistent contestant")
        else:
          print(minimumAverageScore(list,startPosition,finalPosition))
def ui_list(list,command_list,undo_List):
    if(len(command_list)==1):
        displayListScore(list)
    elif(len(command_list)==2 ):
        if(command_list[1]!="sorted"):
            raise Exception("Invalid syntax!")
        else:
           listSorted(list)
           undo_List.append(copy.deepcopy(list))
    elif(len(command_list)==3 and command_list[1]=="<"):
         number=int(command_list[2])
         if (number<0):
             raise Exception("Invalid term of comparation!")
         else:
             listLessThanNumber(list,number)
    elif (len(command_list) == 3 and command_list[1] == "="):
        number = int(command_list[2])
        if (number < 0):
            raise Exception("Invalid term of comparation!")
        else:
            listEqualNumber(list, number)
    elif (len(command_list) == 3 and command_list[1] == ">"):
        number = int(command_list[2])
        if (number < 0):
            raise Exception("Invalid term of comparation!")
        else:
            listGreaterThanNumber(list, number)
    else:
         raise Exception("Invalid syntax!")
def ui_top(list,command_list,undo_List):
    if(len(command_list)==2):
         number=int(command_list[1])
         if(number<0):
             raise Exception("Invalid top!")
         elif(number>len(list)-1):
             raise Exception("Insufficient contestants!")
         else:
             listTop(list,number)
    elif(len(command_list)==3):
        number=int(command_list[1])
        problem=int(command_list[2])
        if (number < 0):
            raise Exception("Invalid top!")
        elif (number > len(list) - 1):
            raise Exception("Insufficient contestants!")
        elif(problem<1 or problem>3):
            raise Exception("Inexistant probe!")
        else:
            listTopProbe(list,number,problem)
    else:
        raise Exception("Invalid syntax")
def ui_undo(list, command_list, undo_List):
   if(len(command_list)==1):
     if(len(undo_List)>1):
       del undo_List[-1]
       list.clear()
       list.extend(undo_List[-1])

     else:
      raise Exception("No more undo is avaiable!")
   else:
       raise Exception("Invalid syntax")




def startConsoleBased():
   list=initialValueScores()
   undo_List=[]
   undo_List.append(initialValueScores())
   functions={
     "add":ui_add,
     "insert":ui_insert,
     "remove":ui_remove,
     "replace":ui_replace,
     "list":ui_list,
     "avg":ui_avg,
     "min":ui_min,
     "top":ui_top,
     "undo":ui_undo
   }
   while(True):
       command=input("Introduce the command:")
       command_list=command.split()
       if command_list[0] == "exit":
           return
       if command_list[0] in functions:
               try:
                   functions[command_list[0]](list, command_list, undo_List)
               except Exception as ex:
                   print(str(ex))
       else:
           print("Invalid command!")

run_all_tests()

