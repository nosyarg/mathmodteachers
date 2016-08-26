#We will assume that this is constant throughout the model.
classesperstudent = 6
#let us start out with a rotate function
def rotate(M,newstud):
        #M should be the class and year matrix, while newstud should be the
        #total number of students who will matriculate at the school next year
        #this function should move each of the students from their current year
        #to the next year and reassign classes appropriately.
        #If I am feeling motivated, I will add the 5% drop
        #note: I was feeling motivated
        #pull in the classes per student global
        global classesperstudent
        #transpose the class matrix
        Mt = zip(*M)
        #find the total number of classes per year and their relative frequencies
        classperyear = []
        classfreqbyyear = []
        for year in Mt:
                classperyear.append(sum(year))
                currentclassfreqs = []
                for val in year:
                        currentclassfreqs.append(val/sum(year))
                classfreqbyyear.append(currentclassfreqs)
        #find the total number of students in each year
        studperyear = []
        for year in classperyear:
                studperyear.append(round(year/classesperstudent))
        #calculate the new number of students in each grade
        newjuniors = round(.95*studperyear[0])
        newseniors = studperyear[1]
        newsophomores = newstud - studperyear[0] - studperyear[1]
        newm = M[:][:]
        #proportionally redistribute students based upon relative class frequencies
        for i in range(len(classfreqbyyear[0])):
                newm[i][0] = round(newsophomores*classesperstudent*classfreqbyyear[0][i]) 
        for i in range(len(classfreqbyyear[1])):
                newm[i][1] = round(newjuniors*classesperstudent*classfreqbyyear[1][i])
        for i in range(len(classfreqbyyear[2])):
                newm[i][2] = round(newseniors*classesperstudent*classfreqbyyear[2][i])
        return newm
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
#find the believed students per year
#studentsperyear = yearclasscounts/classesperstudent
#lets get these new students in there
#start out by finding the relative frequencies of classes by year
print(Matrix)
yearclasscounts = []
Matrixt = zip(*Matrix)
for i in Matrixt:
        yearclasscounts.append(sum(i))
print(yearclasscounts)
for i in range(3):
        Matrix = rotate(Matrix,490)
        Matrixt = zip(*Matrix)
        yearclasscounts = []
        for i in Matrixt:
                yearclasscounts.append(sum(i))
        print(yearclasscounts)
print(Matrix)
