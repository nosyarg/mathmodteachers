#We will assume that this is constant throughout the model.
teachers = [1,4,3,5,1,1,1,6,1,3,5]
dumpfile = 'increase.csv'
classesperstudent = 6.02244898
#let us start out with a rotate function
def roundvect(vect):
        roundedvect = []
        for val in vect:
                roundedvect.append(round(val+.5))
        return roundedvect
def roundmat(mat):
        roundedmat = []
        for row in mat:
                current = []
                for val in row:
                        current.append(round(val+.5))
                roundedmat.append(current)
        return roundedmat
def writematrix(mat,filepath):
        writefile = open(filepath,'w')
        for row in mat:
                for num in row:
                        writefile.write(str(num) + ',')
                writefile.write('\n')
def teachersperstud(mat,teachers):
        ratios = [0]*len(mat)
        for i in range(len(mat)):
                for j in range(len(mat[i])):
                        ratios[i] += mat[i][j]/teachers[i]
        return ratios
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
                studperyear.append(year/classesperstudent)
        #calculate the new number of students in each grade
        newjuniors = (.95*studperyear[0])
        newseniors = studperyear[1]
        newsophomores = newstud - newjuniors - newseniors
        newm = M[:][:]
        #proportionally redistribute students based upon relative class frequencies
        for i in range(len(classfreqbyyear[0])):
                newm[i][0] = (newsophomores*classesperstudent*classfreqbyyear[0][i]) 
        for i in range(len(classfreqbyyear[1])):
                newm[i][1] = (newjuniors*classesperstudent*classfreqbyyear[1][i])
        for i in range(len(classfreqbyyear[2])):
                newm[i][2] = (newseniors*classesperstudent*classfreqbyyear[2][i])
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
allvects = []
print(classes)
allvects.append(classes)
classes =     ['art','bio','che','eng','fre','ger','spa','mat','mus','phy','soc']
newteachers = [  2,    2,    2,    2,    .4,    2,    .6,    2,    2,   2,    2]
allvects.append(newteachers)
for i in range(15):
        if(newteachers[4] == .6):
                newteachers[4] = .4
                newteachers[6] = .6
        elif(newteachers[6] == 1):
                newteachers[4] = .5
                newteachers[6] = .5
        else:
                newteachers[4] = .6
                newteachers[6] = .4
        tempteachers = []
        for i in range(len(teachers)):
                tempteachers.append(teachers[i] + newteachers[i])
        print(roundvect(teachersperstud(Matrix,tempteachers)))
        Matrix = rotate(Matrix,630)
        allvects.append(roundvect(teachersperstud(Matrix,tempteachers)))
writematrix(allvects,dumpfile)
x = 0
for i in Matrix:
        for j in i:
                x += j
print(x)
