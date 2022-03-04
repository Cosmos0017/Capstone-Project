from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


def distance(coord1, coord2) :
        lon1 = radians(coord1[1])
        lon2 = radians(coord2[1])
        lat1 = radians(coord1[0])
        lat2 = radians(coord2[0])
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(a))
        
        r = 6371
        
        return(c * r)

def carGen(n):
        nex = []
        mg = []
        total = 0;
        for i in range(n):
                x = random.randint(1,2)
                if x == 1:
                        nex.append(random.randint(10,30))
                else:
                        mg.append(random.randint(10,30))
        for i in nex:
                k = 100 - i
                total += k*0.75
        
                
        for i in mg:
                k = 100 - i
                total+= k*0.63
                
        return(total)             
                
        
        

if __name__ == "__main__":

        loc = []
        for i in range(2):
                loc.append(float(input()))

        NC = {}


        kensar = pd.read_csv("EVData1 - Sheet1.csv")
        

        for index, row in kensar.iterrows():

                dist = distance(loc, [row['Latitude'], row['Longitude']])
                print(" Distance between current and station number ",index, "is", dist)
                NC[index] = dist;
        coords = []
        NC_sorted = {k: v for k, v in sorted(NC.items(), key=lambda item: item[1])}
        for key, values in NC_sorted.items():
                coords.append([key, values])
        #print(coords)
        print("The closest charging station is at ", coords[0][1], "and is the index number", coords[0][0])

        #random.randint(0,9)
        for i in coords:
                x = random.randint(1,6)
                i.append(x)
                i.append(carGen(x))
        print(coords)
        wt = []
        dist = []
        for i in coords:
                wt.append(i[3])
                dist.append(i[1])
        plt.bar(dist,wt,color = 'maroon', width = 0.4)
        plt.xlabel("No of cars")
        plt.ylabel("Wating time")
        plt.show()
        
                
                








    
