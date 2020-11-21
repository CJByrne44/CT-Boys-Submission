import pandas as pd
import connect_database
#import DataFrame

class find():
    def ref_by_school(self,name):
        for i in range(0,len(df["First"]),1):
            if ((df["First"])[i] == name.split(",")[1]) and ((df["Last"])[i] == name.split(",")[0]):
                self.school=df["University"][i]
                break
        print(self.school)
        self.rows=[]
        for i in range(len(df["University"])):
            if (df["University"])[i]==self.school:
                self.rows.append(i)
        return self.rows

    def total_sort(self,name):
        rows=find.ref_by_school(self,name)
        for i in range(0,len(df["First"]),1):
            if ((df["First"])[i] == name.split(",")[1]) and ((df["Last"])[i] == name.split(",")[0]):
                self.major=df["Major"][i]
                break
        for x in range(len(rows)-1,0,-1):
            #print(df["Major"][rows[x]])
            if df["Major"][rows[x]]!=self.major:
                rows.pop(x)
        for i in rows:
            print(df.loc[i],["Last","First","School","Major"])
            print()
        return


if __name__ == '__main__':
    df = pd.read_csv('people.csv')
    name=input("Name as last,first(no spaces)")
    #df=find.ref_by_school(df)
    x=find.total_sort(df,name)
    print(connect_database)
    #print(x)
    #print(x)