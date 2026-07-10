#SummaryStats

"""This program will get a list of 6 exams from a student user and then
finds the minimum, maximum, and range."""


test1 = int(input("Enter the grade of your first exam."))
test2 = int(input("Enter the grade of your second exam."))
test3 = int(input("Enter the grade of your third exam."))
test4 = int(input("Enter the grade of your fourth exam."))
test5 = int(input("Enter the grade of your fifth exam."))
test6 = int(input("Enter the grade of your sixth exam."))



minimum_test_grade = min(test1, test2, test3, test4, test5, test6)

maximum_test_grade = max(test1, test2, test3, test4, test5, test6)


print("The minimum test score is", minimum_test_grade,".")
print("The maximum test score is", maximum_test_grade,".")

print("The range of test scores is", minimum_test_grade, "through", maximum_test_grade,".")


