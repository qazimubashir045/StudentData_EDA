import pandas as pd
import matplotlib.pyplot as plt
#loading data
data = pd.read_excel('data.xlsx')
# data info
# print(data.head(10))
# print(data.isnull().sum())
# print(data.info())
# print(data.describe())
# filling NaN of parent eduction into unknown
data['Parent Education'].fillna('unknown',inplace=True)
#calculating total average score
avg_score = data['Exam_Score'].mean()
print(f'Average score of all students {avg_score}')
# grouping data according to tutoring or not and exam score
score_comparison_tution = data.groupby('Tutoring')['Exam_Score'].mean()
print(f'Score of tution going and non tutoring is {score_comparison_tution}')
#making bar chart of the score comparison
plt.figure(figsize=(5,5))
plt.bar(score_comparison_tution.index,score_comparison_tution.values, color=['orange','skyblue'])
plt.title('Comparison of Tutoring and NoN-Tutoring Students')
plt.xlabel('Tutoring Or Not')
plt.ylabel('Average Score Scored')
plt.xlim()
plt.ylim(50,90)
plt.grid(color='grey',linestyle='--',linewidth='0.5')
plt.savefig('Tutoring and non-tutoring score.png')
plt.show()
#grouping exam score on the basis of gender
score_comparison_gender = data.groupby('Gender')['Exam_Score'].mean()
print(f'Average Score of Males and Females is {score_comparison_gender}')
#plotting it into bar graph
plt.figure(figsize=(5,5))
plt.bar(score_comparison_gender.index,score_comparison_gender.values,color=['skyblue','orange'])
plt.title('Score Comparison On The Basis of Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score Scored')
plt.xlim()
plt.ylim(50,80)
plt.grid(True, linestyle='--',linewidth='0.5')
plt.savefig('Gender based score comparisn.png')
plt.show()
#now grouping score on the basis of parent education
parent_score = data.groupby('Parent Education')['Exam_Score'].mean()
print(f'Comparison of Score Based on Parent Edcucation is {parent_score}')
#plotting this in horizontal bar graph
plt.barh(parent_score.index,parent_score.values,color=['orange','skyblue','#fc8d62','#e78ac3'])
plt.title('Comparison of Student Scores And There Parent Education')
plt.xlabel('Parent Education')
plt.ylabel('Average Score Of Students')
plt.xlim(50,80)
plt.ylim()
plt.grid(True, linestyle="--",linewidth='0.5')
plt.savefig('Parent education.png')
plt.show()
#based on region
region_score = data.groupby('Region')['Exam_Score'].mean()
print(f'The Score based on Region {region_score}')
#plottting this data into pie
plt.figure(figsize=(5,5))
plt.pie(region_score,labels=region_score.index, autopct='%1.1f%%')
plt.title('Region Based Average Score Of Students')
plt.legend()
plt.savefig('Region Based Score.png')
plt.show()
#grouping data on the bsases of hours studied
hours_and_marks = data.groupby('HoursStudied/Week')['Exam_Score'].mean()
print(hours_and_marks)
#plotting this data into scatter
plt.figure(figsize=(5,5))
plt.scatter(hours_and_marks.index,hours_and_marks.values,color='blue',alpha=0.6)
plt.title('Average Score and The Hours Studied Per Week')
plt.xlabel('Hours Studied Per Week')
plt.ylabel('Average Score Scored')
plt.savefig('Hours And Score.png')
plt.grid(True,linestyle='--',linewidth='0.5')
plt.show()

# EDA by Mubashir Qazi
data.to_excel('Cleaned Data.xlsx')