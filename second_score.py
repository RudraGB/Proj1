students_list =[]
scores_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students_list.append([name,score]) # list for all names and scores
    scores_list.append(score)          # list for all the scores given as input

unique_scores = sorted(set(scores_list), reverse=True) # sorting and creating uniques scores to access the second lowest score
second_score = unique_scores[1]                         # accessing and assigning the second lowest score
print(unique_scores)
for name,score in students_list:                        # comparing the scores in the student list with second lowest score 
    if score == second_score:                           #if they match print the corresponding name
        print(name)
    
        

  
        


        