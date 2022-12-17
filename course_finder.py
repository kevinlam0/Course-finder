# Kevin Lam, mvk2uy

import urllib.request

def instructor_lectures(department, instructor):
    """
    gives all course names for the lectures by the instructor, in the dept
    :param department: the dept of the course (string)
    :param instructor: the instructor we're listing courses for (string)
    :return: list of the courses the instructor teaches
    for lectures only
    if instructor teaches multiple lecutres sections, should only add class name once
    """
    instructor_courses = [] # List to put the course in
    file_read = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" +department) # Opens url file to access into the department chosen 
    for line in file_read: # Reads each line in the file as a loop
        course_list = line.decode('utf-8').strip().split('|') # takes each and decodes the bytes to strings, strips any unwanted elements out of the strings,
        # splits the data by "|" of each line make a list of data

        if course_list[5] == "Lecture" and instructor in course_list[4]  and course_list[0] == department and course_list[3] not in instructor_courses: # The type of class needs to be "Lecture", the instructor, the right department, and the course not already in the list
            instructor_courses.append(course_list[3]) # Adds the course of each line if this if statement is true
    file_read.close
    return instructor_courses


def compatible_classes(first_class, second_class, needs_open_space= False ):
    """
    see if the classes are compatible by seeing if the times overlap.
    also, sees if the classes need open space for enrollment
    :param first_class: one of the classes
    :param second_class: the other class that is being compared with the first class
    :param needs_open_space: does not need open space until the classes are not compatible or the capactiy is reached
    :return: False if they are not compatible, true if they are compatible
    """
    first_class_department = first_class[:first_class.find(" ")] #this creates a string to put into the url for the department
    file_read = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + first_class_department) # Opens url file of the department chosen 
    #make an empty string and empty list, make the first 3 indexes into a string
    first_class_data = [] # List of the first class's data
    empty_list_first =[]

    for line in file_read: #reading each line at a time
        first_class_list = line.decode('utf-8').strip().split('|') #list with the info of class (line)
        tester_string = (first_class_list[0]+" "+first_class_list[1]+"-"+first_class_list[2]) # A string that is compared with the first_class argument
        #to choose the correct class in the file to do the comparison
        if tester_string == first_class: #if they match then use this data and fill the empty string
            first_class_data = first_class_list # Data of this class will occupy first_class_data list
            empty_list_first.append(tester_string)

    second_class_data = []
    empty_list_second = []
    second_class_department = second_class[:second_class.find(" ")]
    file_read = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + second_class_department)
    
    for line in file_read:  # reading each line at a time
        second_class_list = line.decode('utf-8').strip().split('|')  # list with the info of class (line)
        tester_string = (second_class_list[0] + " " + second_class_list[1] + "-" + second_class_list[2]) #String to see if the class is the correct class in the second_class argument
        if tester_string == second_class:
            second_class_data = second_class_list
            empty_list_second.append(tester_string)

    if needs_open_space: # If a True argument is placed into this parameter
        if (int(first_class_data[15]) >= int(first_class_data[16])) or (int(second_class_data[15]) >= int(second_class_data[16])): # Compares the students erolled and enrollment capacity
            return False # If either have reached max capacity, return not compatible automatically

    elif (first_class_data[15] != first_class_data[16]) and (second_class_data[15] != second_class_data[16]): # If they have not reached capacity
        for day in range(7, 12): # Days of the week indexes (Mon-Fri)
            if first_class_data[day] == second_class_data[day] == 'true': # If they both are 'true' that means the class occurs on that day
                if int(second_class_data[12]) <= int(first_class_data[12]) <= int(second_class_data[13]) or int(first_class_data[12])<= int(second_class_data[12]) <= int(first_class_data[13]): #If they start, end, or occur at the same time
                    return False
    file_read.close
    return True # If no False statements are true, then the classes are compatible