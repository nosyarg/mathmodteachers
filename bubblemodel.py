#we are starting out with 490 students
totalstudents = 490
#having the class names could be useful later
classes = ['art','bio','che','eng','fre','ger','spa','mat','mus','phy','soc']
#this is all of the students per year and class. It is organized as classes being broken up in the big array and years in the small array
Matrix = [[31,33,35],[198,95,26],[59,126,109],[183,155,152],[41,32,49],[19,22,10],[51,26,33],[184,201,262],[50,56,49],[50,58,183],[183,131,59]]
#transpose the matrix to simplify future ops and store in new variable
Matrixt = zip(*Matrix)
#find the number of classes taken in total by each year
yearclasscounts = []
for i in Matrixt:
        yearclasscounts.append(sum(i))
#find the total classes taken at the school
totalclasses = sum(yearclasscounts)
#find the average classes per student
classesperstudent = totalclasses/totalstudents
#find the believed students per year
studentsperyear = yearclasscounts/classesperstudent
