class Student:
    def __init__(self, subjects):
        self.subjects = subjects
        self.attendance = {subject: 0 for subject in subjects}
        self.total_classes = {subject: 0 for subject in subjects}

    def mark_attendance(self):
        for subject in self.subjects:
            class_held = input(f"Is the class held for {subject}? (y/n): ")
            if class_held.lower() == "y":
                if subject.endswith("Lab"):
                    is_present = input(f"Are the student present in both classes of {subject}? (y/n): ")
                    if is_present.lower() == "y":
                        self.attendance[subject] += 2
                        self.total_classes[subject] += 2
                    else:
                        self.total_classes[subject] += 2
                else:
                    is_present = input(f"Is the student present in {subject}? (y/n): ")
                    if is_present.lower() == "y":
                        self.attendance[subject] += 1
                        self.total_classes[subject] += 1
                    else:
                        self.total_classes[subject] += 1

    def get_attendance_percentage(self, subject):
        if subject in self.subjects:
            attended_classes = self.attendance[subject]
            total_classes = self.total_classes[subject]
            if total_classes == 0:
                return 0.0
            attendance_percentage = (attended_classes / total_classes) * 100
            return attendance_percentage
        else:
            return 0.0

    def get_overall_attendance_percentage(self):
        total_attended_classes = sum(self.attendance.values())
        total_classes = sum(self.total_classes.values())
        if total_classes == 0:
            return 0.0
        overall_percentage = (total_attended_classes / total_classes) * 100
        return overall_percentage


# Example usage
subjects = ["Hindi", "English", "Maths", "Science", "SST", "OOPS Lab", "OS Lab"]
student = Student(subjects)

while True:
    # Mark attendance for the current day
    student.mark_attendance()

    # Getting subject-wise attendance percentage
    for subject in subjects:
        attendance_percentage = student.get_attendance_percentage(subject)
        print(f"{subject} Attendance Percentage: {attendance_percentage}%")

    # Getting overall attendance percentage
    overall_percentage = student.get_overall_attendance_percentage()
    print(f"Overall Attendance Percentage: {overall_percentage}%")

    # Ask if the user wants to mark attendance for another day
    choice = input("Do you want to mark attendance for another day? (y/n): ")
    if choice.lower() != "y":
        break
