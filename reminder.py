import csv

def main():
    with open ("arrangements.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email_text = create_email(
                row["Teacher"],
                row["Student"],
                row["Subject"],
                row["ExamDate"],
                row["Arrangement"]
            )
            print("--- Draft Email ---")
            print(email_text)
            print()

def create_email(teacher, student, subject, date, arrangement):
    return(
        f"Dear {teacher},\n\n"
        f"Reminder : {student} has a {subject} exam on date {date}.\n"
        f"Please ensure they receive : {arrangement}.\n"
        f"Thanks,\nSenco Lead"
    )

if __name__=="__main__":
    main()

