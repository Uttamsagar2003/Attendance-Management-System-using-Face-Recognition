import os

def clear_attendance():
    # Path to the attendance file
    attendance_file = 'attendance/attendance.csv'

    # Clear the file content
    if not os.path.exists('attendance'):
        os.makedirs('attendance')

    with open(attendance_file, 'w') as f:
        f.write('Name,Time\n')  # Write headers back after clearing

if __name__ == "__main__":
    clear_attendance()
