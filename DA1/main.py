"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 1
Date: 09/12/22
Description: Program relays/analyzes Gonzaga basketball scores. I completed the bonus
"""
import math

# printing og list
print()
list_scores = [2.4, 0.9, 14.1, 0.1, 11.8, 18.4, 7.3, 11.2, 4.3, 0.7, 1.8, 1.0, 11.8, 5.1]
print("Original Score List:", list_scores)
# printing list in reverse BONUS
n = 0
j = len(list_scores)-1
print("Scores in Reverse:", end= '')
while len(list_scores) > n:
    print(" ~", list_scores[j], end= '')
    n+=1
    j-=1
# Computing math values and sorting list in descending order
list_scores.sort(reverse=True)
score_count = sum(list_scores)
avg_score = sum(list_scores)/ len(list_scores)
score_median = len(list_scores)/2
# printing info out to screen
print()
print("Scores in Descending order!:" , list_scores)
print("Count of Numbers:" ,f"{score_count:.2f}")
print("Average of Scores:" ,f"{avg_score:.2f}")
print("Median of Scores:" , round(score_median))
print("Smallest of Scores:" , list_scores[len(list_scores)-1])
print("Largest of Scores:" , list_scores[0])
print()
# Asking user to enter their own info with a error check
print("--- ADD YOUR OWN SCORE ---")
user_score = float(input("Please enter the score you would like to put in the list: "))
user_index = int(input("Now enter where you want it in the list: "))
if 0 <= user_index <= len(list_scores):
    print()
    print("--- YOUR NEW LIST ---")
    list_scores[user_index-1] = user_score
    print(list_scores)
else:
    print("please enter a valid index")
