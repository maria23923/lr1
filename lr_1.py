# Part 4
# Створюємо словник
students = {}
for i, name in enumerate(student_names):
    students[name] = {
        "math": math_grades[i],
        "statistics": statistics_grades[i],
        "physics": physics_grades[i],
    }

# 1. Вивід статистики по кожному студенту
print("\nMiddle marks")
averages = {}
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    averages[name] = avg
    print(f"student: {name}, mark:{avg:.2f}")

# 2. Топ-3 студенти
print("\nTop 3 students")
top3 = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]
for i, (name, avg) in enumerate(top3, start=1):
    print(f"{i}. {name} (middle {avg:.2f})")

# 3. Загальна статистика
print("\nAll statistics")
print(f"Students {len(student_names)}")

subjects = ["math", "statistics", "physics"]
for subj in subjects:
    grades = [students[name][subj] for name in student_names]
    avg = sum(grades) / len(grades)
    print(f"{subj}: middle mark {avg:.2f}, min: {min(grades)}, max: {max(grades)}")

# 4. Студенти з найвищим балом у кожному предметі
print("\nBest marks in subjects")
for subj in subjects:
    best_name = max(student_names, key=lambda name: students[name][subj])
    best_grade = students[best_name][subj]
    print(f"{subj}: student {best_name}, оцінка: {best_grade}")

# 5. Студенти з середньою < 50
print("\n Students with average < 50")
low = [name for name, avg in averages.items() if avg < 50]
print(f"Number of students {len(low)}")
for name in low:
    print(name)

