import os
import math
class form:
    def freq(self,i):
        freq_l=[]
        freq_dic={}
        freq_f=open(i,"r")
        for line in freq_f:
            line=line.replace("."," ").replace(","," ")
            for word in line.split():
                a=word.lower()
                freq_l.append(a)
        for j in freq_l:
            if j not in freq_dic:
                freq_dic[j]=1
            else:
                freq_dic[j]+=1
        freq_f.close()
        return freq_dic
    def dot(self,x,y):
        dot_sum=0
        for i in x:
            for j in y:
                if i==j:
                    m=x[i]*y[j]
                    dot_sum=dot_sum+m
        return dot_sum

    def norm(self,n1,n2):
        n_s1=0
        n_s2=0
        for i in n1:
            n_s1=n_s1+(n1[i]**2)
        for j in n2:
            n_s2=n_s2+(n2[j]**2)
        m1=math.sqrt(n_s1)
        m2=math.sqrt(n_s2)
        return (m1*m2)
    def result(self,s,n):
        r1=round((s/n)*100)
        if r1==0:
            return 1.57
        return r1
class call:
    def calls(self,a):
        r=[]
        r1=[]
        for m in range(0,len(a),1):
            for n in range(0,len(a),1):
                if m==n:
                    r1.append(None)
                else:
                    r.append(fo.freq(a[m]))
                    r.append(fo.freq(a[n]))
                    
                    d1=fo.dot(r[0],r[1])
                    n=fo.norm(r[0],r[1])
                    
                    r1.append(fo.result(d1,n))
                    r=[]
            print(a[m],r1,"\n")
            r1=[]
n=input("Enter the directory\n")
a=os.listdir(n)
le=len(a)
os.chdir(n)
ca=call()
fo=form()
ca.calls(a)

