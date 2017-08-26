########################################################################################################################################################
# string matching.py                                                                                                                                   #
# AUTHOR:       THOTA SHARATH                                                                                                                          #
# DATE:         CREATED: 24/08/2017                                                                                                                    #
# BRIEF:        Plagiarism Detector                                                                                                                    #
#               It compares the character by character and print the result in matrix                                                                  #
########################################################################################################################################################


import os
import string
class LCS:
    def __init__(self,a):
        self.a=a
    def string_pun(self,f_n):
        s=""                                                            # File list
        f=open(f_n,"r")
        for line in f:                                                  # Reading each line in file
            for c in string.punctuation:      
                if c!='_':
                    line=line.replace(c,"")                             # Replacing the punctuation 
            #for word in line.split():
            a=line.lower()                                              # Converting all letters into lowercase
            s=s+a
        return s                                                    
    def com_substring(self,a1,b1):                                      # Method is used to find common substring           
        m=len(a1)
        n=len(b1)
        max=0
        s=""
        for i in range(0,m,1):                                      
            pos=i                                                       # Assiging the value of i to another variable
            for j in range(0,n,1):
                if pos<m:
                    if a1[pos]==b1[j]:                                  # Checking the characters are equal or not
                        pos=pos+1
                        if (pos-i)>max:
                            max=pos-i
                            s=a1[i:pos]                                 # Storing the longest substring in s
                    else:
                        pos=i
                   
        return max,s
    def per(self,a1,b,c):                                               # Claculating the percentage
        try:
            r=((c*2)/(a1+b))*100
            return round(r)
        except ZeroDivisionError:
            return 0
            
    def files_read(self,a):
        d1=[]
        for i in range(0,len(a),1):
            for j in range(0,len(a),1):
                if i==j:
                    d1.append(None)                                     # For same file comparision result set to None
                else:
                    a1=LC.string_pun(a[i])
                                                                        # Sending the first file name
                    b1=LC.string_pun(a[j])                              # Sending the second file name
                    c1=LC.com_substring(a1,b1)
                    d1.append(LC.per(len(a1),len(b1),int(c1[0])))
            print(a[i],c1[1],d1)
            d1=[]
n=input("Enter the directory\n")
a=os.listdir(n)                                                         #it stores the all files in the directry in list a
os.chdir(n)                                                             #changing the default system path to user entered path
LC=LCS(a)                                                               # Creating an object for LCS Class
LC.files_read(a)                                                        #By using LCS object calling the files_read function
