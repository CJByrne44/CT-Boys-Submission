import pandas as pd
#import DataFrame

class find():
    def ref_by_school(self,name):
        for i in range(0,len(df["First"]),1):
            if ((df["First"])[i] == name.split(",")[1]) and ((df["Last"])[i] == name.split(",")[0]):
                self.school=df["School"][i]
                break
        print(self.school)
        self.rows=[]
        for i in range(len(df["School"])):
            if (df["School"])[i]==self.school:
                self.rows.append(i)
        return self.rows

    def total_sort(self,name):
        rows=find.ref_by_school(self,name)
        for i in range(0,len(df["First"]),1):
            if ((df["First"])[i] == name.split(",")[1]) and ((df["Last"])[i] == name.split(",")[0]):
                self.major=df["Major"][i]
                break
        for x in range(len(rows)-1,0,-1):
            if df["Major"][rows[x]]!=self.major:
                rows.pop(x)
        for i in rows:
            print(df.loc[i],["Last","First","School","Major"])
            print()
        return


if __name__ == '__main__':
<<<<<<< HEAD
    df = pd.read_csv('C:\Users\ujali\Downloads\SPOILER_people (2).csv')
=======
    df = pd.read_csv('people.csv')
>>>>>>> 684cdc077c035d32167b47d752e872f796604be8
    name=input("Name as last,first(no spaces)")
    #df=find.ref_by_school(df)
    x=find.total_sort(df,name)
    #print(x)
    #print(x)

