'''
Hey!

I'm trying to make a program that will make a .txt file, ask the user (who is a teacher) for
their name, the class they teach, and how long they teach for. Finally, I want the program to 
add that info to the .txt file. However, everything feels broken. Can you help me please?
'''

def main():
    #Creates a file called "Teacher_file.txt" in the directory that your program is in.
    teacher_txt_file = open("Teacher_file.txt", 'w')

    #Receives the teacher's name and puts it in the txt file
    teacher_name = input("Please enter the teacher's name: ")
    teacher_txt_file.write(teacher_name + "\n")

    #Receives the teacher's subject and puts it in the txt file
    subject_taught = input("Please enter the subject that you teach: ")
    teacher_txt_file.write(subject_taught + "\n")

    #Receives the teacher's teaching hours and puts it in the txt file
    teaching_hours = input("How long do you work for every day, in hours: ")
    teacher_txt_file.write(teaching_hours + "\n")

    #Closes the .txt file, so the data can be saved.
    teacher_txt_file.close()

main()
    
