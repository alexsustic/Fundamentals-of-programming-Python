from getset import*
""" This function creates a new contestant and his scores 
    input: score1,score2,score3
    output:a list representing the new contestant
"""
def createContestantScore(score1=0,score2=0,score3=0):
      data=[0,0,0]
      setContestantScore1(data,score1)
      setContestantScore2(data,score2)
      setContestantScore3(data,score3)
      return data
    
""" This function creates ten inital contestants and their scores 
     input: -
     output: the score list of the initial contestants
"""
def initialValueScores():
      scoreList=[]
      scoreList.append(createContestantScore(5,7,8))
      scoreList.append(createContestantScore(8,9,10))
      scoreList.append(createContestantScore(3,5,6))
      scoreList.append(createContestantScore(1,2,3))
      scoreList.append(createContestantScore(3,5,7))
      scoreList.append(createContestantScore(2,4,6))
      scoreList.append(createContestantScore(10,10,5))
      scoreList.append(createContestantScore(9,9,4))
      scoreList.append(createContestantScore(10,6,10))
      scoreList.append(createContestantScore(5,6,8))
      return scoreList
    
"""This function displays on the UI interface the contestants and their scores
   input: list - the list of the contestants and their scores
   output: list- the list of the contestants and thei scores
"""

def displayListScore(list):
      print(list)
      
"""This function inserts a new participant and his scores in the list of the contestants 
   input:list - the list of the contestants and their scores
         score1,score2,score3
   output: -
"""
def add(list,score1,score2,score3):
    list.append(createContestantScore(score1,score2,score3))
    
"""This function inserts a new participant and his scores on a certain position in the list of the contestants 
   input:list (list of contestants), position(where to add the new contestant),score1,score2,score3
   output: -
"""
def insert(list,position,score1,score2,score3):
    list.insert(position,createContestantScore(score1,score2,score3))
    
"""This function set the scores to 0 to all the participants starting from position 1 to position 2
   input:list(list of contestants), position1(the beginning position), position2(the final position)
   output: -
"""
def remove(list,startPosition,finalPosition):
    for i in range(startPosition,finalPosition+1):
        del list[i]
        list.insert(i,[0,0,0])
        
""" This function changes the score of a contestant at a certain probe based on his position in the list
    input:list(list of contestants), position(to whom contestant to change score), probe(at which probe) , newScore
    output: -
"""
def replace(list,position,problem,newScore):
    problem=problem-1
    list[position][problem]=newScore
    
""" This function displays the list of participants and their scores for each problem
    input: list(list of contestants)
    output: -
"""
def List(list):
    print(list)
    
""" This function calculates the average score of a certain contestant based on his position
    input:list(list of contestants),position(which contestant)
    output: avScore(average score of that contestant)
"""
def averageScore(list,position):
    avScore=((list[position][0]+list[position][1]+list[position][2])/3)
    return avScore

""" This function writes the participants sorted in decreasing order of their average score and modify the original list of contestants
   input:list(list of contestants)
   output: -
"""
def listSorted(list):
    
    for i in range(0,len(list)):
       for j in range(0,len(list)):
         if(averageScore(list,i)>averageScore(list,j)):
              auxiliaryVariable=list[i]
              list[i]=list[j]
              list[j]=auxiliaryVariable
    
"""This function displays the participants having an average score less than a certain number
   input:list(list of contestants),number(number of comparation)
   output: -
"""
def listLessThanNumber(list,number):
    for i in range(0,len(list)):
         if(averageScore(list,i)<number):
             print(list[i])
             
"""This function writes the participants having an average score equal with a certain number
   input:list(list of contestants),number(number of comparation)
   output: -
"""
def listEqualNumber(list,number):
    for i in range(0,len(list)):
         if(averageScore(list,i)==number):
             print(list[i])
             
"""This function writes the participants having an average score greater than a certain number
   input:list(list of contestants),number(number of comparation)
   output: -
"""
def listGreaterThanNumber(list,number):
    for i in range(0,len(list)):
         if(averageScore(list,i)>number):
             print(list[i])
""" This function returns the average of the average scores of the contestants from position 1 to position2
    input:list(list of contestants),position1(from which contestant),position2(to which contestant)
    output: the average of the average scores
"""
def averageOfAverageListScore(list,startPosition,finalPosition):
    sum=0
    numberContestants = finalPosition - startPosition + 1
    for i in range(startPosition,finalPosition+1):
        sum=sum+averageScore(list,i)
    return sum/numberContestants
"""This function returns the minimum average score of the contestants from position1 to position2
   input:list(list of contestants),position1(from which contestant),position2(to which contestant)
   output:minimumAv(the minimum average score)
"""
def minimumAverageScore(list,startPosition,finalPosition):
    minimumAv=10
    for i in range(startPosition,finalPosition+1):
        if(averageScore(list,i)<minimumAv):
            minimumAv=averageScore(list,i)
    return minimumAv
"""This function displays the top of the contestants which have the biggest average score in the descending order 
   input:list(list of contestants),number(the number of contestants in the top)
   output:-
"""
def listTop(list,number):
    copyList=list.copy()
    listSorted(copyList)
    for i in range(0,number):
      print(copyList[i])
"""This function displays the top of the contestants which have the biggest average score in the descending order at a certain probe
   input:list(list of contestants),number(the number of contestants in the top),probe(at which probe)
   output:-
"""
def listTopProbe(list,number,problem):
    copyList=[]
    problem=problem-1
    copyList=list.copy()
    for i in range(0,len(copyList)):
      for j in range(0,len(copyList)):
          if(copyList[i][problem]>copyList[j][problem]):
              auxiliary=copyList[i][problem]
              copyList[i][problem]=copyList[j][problem]
              copyList[j][problem]=auxiliary
    for k in range (0,number):
        print(copyList[k])
"""
This function set the scores of the contestants to 0 if the average score of their scores is less than a certain number
input:list(list of contestants),number(number of comparation)
output:-
"""
def removeLessThanANumber(list,number):
    for i in range(0,len(list)):
      if(averageScore(list,i)<number):
         list[i][0]=0
         list[i][1]=0
         list[i][2]=0
"""This function set the scores of the contestants to 0 if the average score of their scores is equal with a certain number
   input:list(list of contestants),number(number of comparation)
   output:-
"""
def removeEqualToANumber(list,number):
    for i in range(0,len(list)):
      if(averageScore(list,i)==number):
         list[i][0]=0
         list[i][1]=0
         list[i][2]=0
"""This function set the scores of the contestants to 0 if the average score of their scores is greater than a certain number
   input:list(list of contestants),number(number of comparation)
   output:-
"""
def removeGreaterThanANumber(list,number):
    for i in range(0,len(list)):
      if(averageScore(list,i)>number):
         list[i][0]=0
         list[i][1]=0
         list[i][2]=0
def print_menu():
   print("1.Add the result of a new participant")
   print("2.Display the score list")
   print("3.Modify the scores")
   print("4.Display the participants whose score has different properties")
   print("5.Obtain different characteristics of participants")
   print("6.Establish the podium")
   print("7.Undo the last operation performed")
   print("8.Exit")
   
def print_menu_add():
   print("1.Add the scores of the new participant")
   print("2.Add the scores of the new participant at a certain position")
   
def print_menu_change_scores():
   print("1.Change the score of the contestant to 0")
   print("2.Replace the score of a contestant at a certain probe")
   
def print_menu_score_proprieties():
    print("1.Display the score list")
    print("2.Display the participants sorted in decreasing order of their average score")
    print("3.Write the participants whose scores respect a given propriety")

def print_menu_score_proprieties_3():
    print("1.Display the participants with average score less than a number")
    print("2.Display the participants with average score equal with a number")
    print("3.Display the participants with average score greater than a number")
def print_menu_characteristic_participants():
    print("1.Display average score from position1 to position2:")
    print("2.Display the lowest average score between position1 to position2:")
def print_menu_establish_podium():
    print("1.Display the n participants having the highest average score, in descending order of their average score")
    print("2.Display the n participants who obtained the highest score for a certain probe, sorted descending by that score")
    print("3.Set the scores of participants having an average score less than a number to 0")
    print("4.Set the scores of participants having an average score equal to a number to 0")
    print("5.Set the scores of participants having an average score greater than a number to 0")