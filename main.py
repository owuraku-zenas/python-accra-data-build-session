import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
df = pd.read_csv('student_results.csv')

# Calculate average scores
average_scores = df[['Math Score', 'Science Score', 'English Score', 'History Score']].mean()

print("Average Scores:")
print(average_scores)


# Plot the average scores
plt.figure(figsize=(10, 6))
average_scores.plot(kind='bar', color='skyblue')
plt.title('Average Scores by Subject')
plt.ylabel('Average Score')
plt.xlabel('Subject')
plt.xticks(rotation=0)  # Rotate x labels for better readability
plt.ylim(0, 100)  # Set y-axis limit
plt.savefig('results/average_scores.png')



scores = df[['Math Score', 'Science Score', 'English Score', 'History Score']].columns
grouped_by_grade =  df.groupby('Grade')[scores].mean()

print(grouped_by_grade)

# Plot the average scores by grade for each subject
grouped_by_grade.plot(kind='bar', figsize=(12, 8), color=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow'])
plt.title('Average Scores by Subject and Grade')
plt.ylabel('Average Score')
plt.xlabel('Grade')
plt.xticks(rotation=0)  # Rotate x labels for better readability
plt.ylim(0, 100)  # Set y-axis limit
plt.legend(title='Subject')
plt.grid(axis='y')

# Save the plot to a file
plt.savefig('results/average_scores_by_grade.png')



# Convert Grade and Term to a single time variable (e.g., Year-Term)
df['Time'] = df['Grade'].astype(str) + '-' + df['Term'].astype(str)

# Sort by the new Time variable
df.sort_values(by='Time', inplace=True)

# Set the Time variable as the index
df.set_index('Time', inplace=True)


# Plot the scores over time
plt.figure(figsize=(12, 8))
plt.plot(df.index, df['Math Score'], marker='o', label='Math')
plt.plot(df.index, df['Science Score'], marker='*', label='Science')
plt.plot(df.index, df['English Score'], marker='', label='English')
plt.plot(df.index, df['History Score'], marker='+', label='History')

plt.title('Student Performance Over Time')
plt.xlabel('Time (Grade-Term)')
plt.ylabel('Scores')
plt.ylim(65, 100)  # Set y-axis limit
plt.legend()
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.tight_layout()

# Save the plot to a file
plt.savefig('results/student_performance_over_time.png')





# Select columns for study habits and performance scores
study_habits = ['Math Extra Classes', 'Science Extra Classes', 'English Extra Classes', 'History Extra Classes', 'Study Hours per Week']
performance_scores = ['Math Score', 'Science Score', 'English Score', 'History Score']

# Calculate the correlation matrix
correlation_matrix = df[study_habits + performance_scores].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Study Habits and Performance')
plt.show()

# Save the heatmap to a file
plt.savefig('results/study_habits_performance_correlation.png')





# Calculate average scores for each study habit
average_scores_by_study_hours = df.groupby('Study Hours per Week')[['Math Score', 'Science Score', 'English Score', 'History Score']].mean()

print("Average Scores by Study Hours per Week:")
print(average_scores_by_study_hours)

# Plotting the average scores by study hours
plt.figure(figsize=(10, 6))

for subject in ['Math Score', 'Science Score', 'English Score', 'History Score']:
    plt.plot(average_scores_by_study_hours.index, average_scores_by_study_hours[subject], marker='o', label=subject)

plt.xlabel('Study Hours per Week')
plt.ylabel('Average Score')
plt.title('Average Scores by Study Hours per Week')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('results/average_scores_by_study_hours.png')
plt.show()




# Calculate the standard deviation of scores across terms
variability = df.groupby('Term')[['Math Score', 'Science Score', 'English Score', 'History Score']].std()

print("Performance Variability Across Terms:")
print(variability)

# Plot the variability
plt.figure(figsize=(14, 8))

for subject in ['Math Score', 'Science Score', 'English Score', 'History Score']:
    plt.plot(variability.index, variability[subject], marker='o', label=subject)

plt.xlabel('Term')
plt.ylabel('Standard Deviation')
plt.title('Performance Variability Across Terms')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('results/performance_variability_across_terms.png')
plt.show()



# Calculate raw scores by grade
score_columns = ['Math Score', 'Science Score', 'English Score', 'History Score']
raw_scores_by_grade = df.groupby('Grade')[score_columns].sum()

# Plot pie charts for each grade
num_grades = raw_scores_by_grade.shape[0]
fig, axes = plt.subplots(1, num_grades, figsize=(20, 6), sharey=True)

for i, grade in enumerate(raw_scores_by_grade.index):
    scores = raw_scores_by_grade.loc[grade]
    axes[i].pie(scores, labels=scores.index, autopct='%1.1f%%', startangle=140)
    axes[i].set_title(f'Grade {grade}')

plt.tight_layout()
plt.savefig('results/raw_scores_by_grade.png')
plt.show()




# Determine if extra classes were attended
extra_classes_columns = ['Math Extra Classes', 'Science Extra Classes', 'English Extra Classes', 'History Extra Classes']
df['Attended Extra Classes'] = df[extra_classes_columns].gt(0).any(axis=1)

# Calculate average scores based on extra classes attendance
performance_by_extra_classes = df.groupby('Attended Extra Classes')[['Math Score', 'Science Score', 'English Score', 'History Score']].mean()

print("Average Scores Based on Extra Classes Attendance:")
print(performance_by_extra_classes)

# Plot the results
fig, ax = plt.subplots(figsize=(12, 8))

performance_by_extra_classes.plot(kind='bar', ax=ax)
ax.set_xlabel('Attended Extra Classes')
ax.set_ylabel('Average Score')
ax.set_title('Average Scores Based on Extra Classes Attendance')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('results/performance_by_extra_classes.png')
