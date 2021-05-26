#violent_crimes_plot.py
import matplotlib.pyplot as plt
 
violentCrimesFile= open('crimes.txt')
crimesList= violentCrimesFile.readlines()
#print(crimesList)
 
#convert the crimeList from strings to integers
for i in range(len(crimesList)):
    crimesList[i] = int(crimesList[i])
 
print(crimesList)
 
dates= range(2000,2020)
 
for i in dates:
    print(i)
 
plt.plot(dates,crimesList,'rp--')
plt.title("Violent Crimes 2000-2019")
 
plt.xlabel("Time(years)")
 
plt.ylabel("Crimes millions")
plt.xticks([2000,2004,2008,2012,2016,2020])
plt.show()
 
 
 
