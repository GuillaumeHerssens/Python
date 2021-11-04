def school():
    roster = {"Bob" : 1,"Ernest" : 4, "Alice" : 1, "Charlie" : 2,"Joshua" : 1, "David" : 3,"Hector" : 2}    
    while True:
        selection = input("Input your selection :\n1. Add student.\n2. Student list by grade.\n3. List of all students.\n4. Exit.\n")        
        
        if selection == "1":
            add_name = input("Input student name :")
            add_grade = int(input("Input student grade :"))
            roster[add_name] = add_grade

        elif selection =="2":
            grade = int(input("Input student grade :"))
            grades_name = []
            for i, j in roster.items():
                if j == grade:
                    grades_name.append(i)
            grades_name.sort()
            print ("\nStudents in grade %s :" % (grade))
            print (*grades_name, sep = ", ")


        elif selection == "3":
            grades = list(set(roster.values()))
            for g in range(1,len(grades)+1):
                grades_name = []
                for i, j in roster.items():
                    if j == g:
                        grades_name.append(i)
                grades_name.sort()
                print ("\nStudents in grade %s :" % (g))
                print (*grades_name, sep = ", ")
        elif selection == "4":
            break
        else:
            print ("\nInvalid input, try again.\n")

school()
