num_scores = int(input("Enter the number of scores: "))
scores_list = []
for each in range(num_scores):
    score = int(input(f"Enter score # {each + 1}: "))
    while score < 0 or score > 100:
        print("Score is invalid.")
        print("Score must be between 0 and 100.")
        score = int(input(f"Enter score # {each + 1} again: "))
    scores_list.append(score)
print("Scores entered:", scores_list)
lowest_score = min(scores_list)
scores_list.remove(lowest_score)
average_score = sum(scores_list) / len(scores_list)
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(f"The average score after removing the lowest score is: {average_score:.2f}")
print(f"The letter grade is: {letter_grade}")