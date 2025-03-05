class AttendanceSystem:
    def __init__(self):
        self.students = set()  # Store student names
        self.attendance = {}   # Dictionary to track attendance

    def add_student(self, name):
        """Adds a student to the system."""
        self.students.add(name)
        self.attendance[name] = set()
        print(f"Student '{name}' added successfully!")

    def mark_attendance(self, name, date):
        """Marks attendance for a student on a given date."""
        if name in self.students:
            self.attendance[name].add(date)
            print(f"Attendance marked for {name} on {date}")
        else:
            print("Student not found! Please add the student first.")

    def view_attendance(self, name):
        """Displays the attendance record for a student."""
        if name in self.students:
            dates = self.attendance[name]
            if dates:
                print(f"{name}'s Attendance: {', '.join(dates)}")
            else:
                print(f"No attendance recorded for {name}.")
        else:
            print("Student not found!")

    def generate_report(self):
        """Generates an attendance report for all students."""
        print("\nAttendance Report:")
        for student in self.students:
            dates = ", ".join(self.attendance[student]) if self.attendance[student] else "No attendance recorded"
            print(f"{student}: {dates}")

# Main Execution
def main():
    system = AttendanceSystem()
    
    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            system.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            system.mark_attendance(name, date)
        elif choice == '3':
            name = input("Enter student name: ")
            system.view_attendance(name)
        elif choice == '4':
            system.generate_report()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
