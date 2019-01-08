import csv


class csv_dataset:
    def __init__(self,fil):
        f = open(fil,'r')
        fread = csv.reader(f)
        rowdata = list(fread)
        self.data = rowdata[1:]
     
    def calc_diff(self):
        dif = [abs(int(row[5]) -  int(row[6])) for row in self.data ]
        return dif
    
    def calc_min(self):
        minimo = [i for i,value in enumerate(self.calc_diff()) if value==min(self.calc_diff())]
        return minimo
    
    def get_team(self):
        ind_min = self.calc_min()[0]
        team = self.data[ind_min][0]
        return team

data = csv_dataset("C:/python/Projects/football.csv")

print(data.get_team())
        