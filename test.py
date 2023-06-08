import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# ds = pd.read_csv("IntelSC.csv")
# X = ds.drop(columns=['Overall','Mindset .1','Creativity','Personality.1','Timing'])
# y = ds['Overall']

# model = DecisionTreeClassifier()
# model.fit(X,y)

# excel to input data
a = pd.read_excel("inputtrial1data.xlsx")
FID = []
NameCol = list(a['Name'])
AcademicsCol = list(a['Academics'])
CreativityCol = list(a['Creativity '])
LeadershipCol = list(a['Leadership '])
MindsetCol = list(a['Mindset '])
TimingCol = list(a['Timing '])
PersonalityCol = list(a['Personality'])
SCHOOLECCol = list(a['SCHOOL EC'])
OUTSIDEECCol = list(a['OUTSIDE EC'])
for x in range(len(NameCol)):
    FID.append(
        [NameCol[x], AcademicsCol[x], CreativityCol[x], LeadershipCol[x], LeadershipCol[x], MindsetCol[x], TimingCol[x],
         PersonalityCol[x], SCHOOLECCol[x], OUTSIDEECCol[x]])

model = joblib.load('scholifydata.joblib')
while True:
    s = int(input("Enter values for result output of Overall, Mindset, Creativity, Personality,Timing press 0,1,2,3,4: "))
    if s == 0:
        for z in FID:
            predict = model.predict([[z[1], z[2], z[3], z[4], z[5], z[6], z[7], z[8]]])
            pl = list(predict)
            if pl[0] == 'Selected':
                print(f"{z[0]} {pl[0]} in overall")
    elif s == 1:
        for z1 in FID:
            if z1[1] >= 20:
                print(f"{z1[0]} Selected For Mindset")
    elif s == 2:
        for z2 in FID:
            if z2[2] >= 20:
                print(f"{z2[0]} Selected For Creativity")
    elif s == 3:
        for z3 in FID:
            if z3[7] >= 90:
                print(f"{z3[0]} Selected For Personality")
    elif s == 4:
        for z4 in FID:
            if z4[6] >= 40:
                print(f"{z4[0]} Selected For Timing")


