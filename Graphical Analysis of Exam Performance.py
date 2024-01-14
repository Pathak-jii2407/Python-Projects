import os
import pandas as pd 
import matplotlib.pyplot as pl
import numpy as np


path = 'E:\\result'

class Manage:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    
    def __str__(self):

        try:
            if os.path.exists(path):
                print("Directory already exists")
            else:
                os.makedirs(path)
                print("Directory created successfully")

        except Exception as e:
            print(f'Error: {e}')
    def get_user_id():
        forgot_name=input("Enter user name: ")
        forgot_number=int(input("Enter user Phone number: "))
        while len(forgot_number) != 10:
            print(f"Phone number must be 10 digits long.\tYou Enterd {len(forgot_number)}")
            forgot_number = input("Enter phone number: ")
        print(f'Your student Id is: {forgot_name}@{forgot_number[6:]} (Please Remember!)')
                
        


    
    def makefile(self):
        name=self.name
        phone=self.phone
        global file_name,main_name
        main_name=f'{name}@{phone[6:]}'
        file_name=f'E:\\result\\{main_name}.csv'
        if os.path.exists(file_name):
            print("You Already Login\n")
            quit=input('Enter < 0 > to Re-Fill: < u > to Update: < r > to see Result: ')
            if quit =='0':
                return main()    
            elif quit.lower()=='u':
                return exam_input()
            else:
                user_id=input("Enter your-id (if forgot enter < 0 >):\n\n")
                if user_id=='0':
                    Manage.get_user_id()
                search_=f'{path}//{user_id}.csv'
                df=pd.read_csv(search_)
                sub_h=[]
                sub_a=[]
                sub_q=[]
                for i in range(5):
                    sub_q.append(df['Quarterly'][i])
                    sub_h.append(df['Half Yearly'][i])
                    sub_a.append(df['Annual'][i])
                    i+=1
                strt=[0,1,2,3,4,]
                pl.plot(strt,sub_q,'orange',linewidth=1,label='Quarterly')
                pl.plot(strt,sub_h,'green',linewidth=1,label='HalfYearly')
                pl.plot(strt,sub_a,'blue',linewidth=1,label='Annual')
                
                
                pl.plot(np.concatenate([sub_h[:4],sub_a[:4]]),'purple',linewidth=4,marker='*',markersize=2,markeredgecolor='red',label='Result')
                
                pl.xlabel("Data")
                pl.ylabel("Score")
                pl.legend(loc=4)
                pl.show()
                                

                
                return main()
                    
        else:
            print(f'Your student Id is: {name}@{phone[6:]} (Please Remember!)')
            
class Graph:
    
    def __init__(self, math_Q,physic_Q,chemistry_Q,hindi_Q,english_Q,
        math_H,physic_H,chemistry_H,hindi_H,english_H,
        math_A,physic_A,chemistry_A,hindi_A,english_A,test):
        
        self.maths_q=math_Q
        self.phy_q=physic_Q
        self.che_q=chemistry_Q
        self.hin_q=hindi_Q
        self.eng_q=english_Q
        self.math_a=math_A
        self.math_h=math_H
        self.phy_h=physic_H
        self.phy_a=physic_A
        self.che_h=chemistry_H
        self.che_a=chemistry_A
        self.hin_h=hindi_H
        self.hin_a=hindi_A
        self.eng_h=english_H
        self.eng_a=english_A
        self.test=test
        
    
    
    def save_data(self):
        score=[]
        
        Data = {
            'Quarterly':{
                "Math":self.maths_q,
                "Physics":self.phy_q,
                "Chemistry":self.che_q,
                "Hindi":self.hin_q,
                "English":self.eng_q
                },
            'Half Yearly':{
                "Math":self.math_h,
                "Physics":self.phy_h,
                "Chemistry":self.che_h,
                "Hindi":self.hin_h,
                "English":self.eng_h
                },
            'Annual':{
                "Math":self.math_a,
                "Physics":self.phy_a,
                "Chemistry":self.che_a,
                "Hindi":self.hin_a,
                "English":self.eng_a
                }
        }
        add_result_Q=self.maths_q+self.phy_q+self.che_q+self.hin_q+self.eng_q
        percentage_Q=add_result_Q/5
        total_Q= f"{percentage_Q}%"
        
        add_result_H=self.math_h+self.phy_h+self.che_h+self.hin_h+self.eng_h
        percentage_H=add_result_H/5
        total_H=f"{percentage_H}%"
        
        add_result_A=self.math_a+self.phy_a+self.che_a+self.hin_a+self.eng_h
        percentage_A=add_result_A/5
        total_A= f"{percentage_A}%"
        
        percentage={
            'Quarterly':total_Q,
            'Half Yearly':total_H,
            'Annual':total_A
        }
        
        df=pd.DataFrame(Data)
        df1=pd.DataFrame(percentage,index=['%'])
        Final=pd.concat([df,df1])
        Final.to_csv(file_name,index=True)
        
        graph_result_Q=[0,self.maths_q,self.phy_q,self.che_q,self.hin_q,self.eng_q]
        graph_result_A=[0,self.math_a,self.phy_a,self.che_a,self.hin_a,self.eng_h]
        graph_result_H=[0,self.math_h,self.phy_h,self.che_h,self.hin_h,self.eng_h]

        strt=[0,1,2,3,4,5]
        #all exam
        pl.plot(strt,graph_result_Q,'orange',linewidth=1,label='Quarterly')
        pl.plot(strt,graph_result_H,'green',linewidth=1,label='HalfYearly')
        pl.plot(strt,graph_result_A,'blue',linewidth=1,label='Annual')
        
        
        
        #sum

        
        # main score
        if graph_result_A and graph_result_H != [0,0,0,0,0,0]:
            graph_result_A.remove(0)
            graph_result_H.remove(0)
            score=np.concatenate([graph_result_Q[:2],graph_result_H[:2],graph_result_A[:2]])
            score+=20   
        else:
            score=np.concatenate([graph_result_Q,graph_result_H,graph_result_A,self.test])
            score-=20
        print(score)
        
        
        pl.plot(score,'purple',linewidth=4,marker='*',markersize=2,markeredgecolor='red',label='Result')
        pl.xlabel("Data")
        pl.ylabel("Score")
        pl.legend(loc=4)

        
        pl.show()
        
        
        
        

    
    
        

class Single_exam:
    def __init__(self,maths,phy,chem,hin,eng):
        self.maths_q=maths
        self.phy_q=phy
        self.che_q=chem
        self.hin_q=hin
        self.eng_q=eng
        
    def single_exam(self):
        math_Q=self.maths_q
        physic_Q=self.phy_q
        chemistry_Q=self.che_q
        hindi_Q=self.hin_q
        english_Q=self.eng_q
        add_result=math_Q+physic_Q+chemistry_Q+hindi_Q+english_Q
        percentage=add_result/5
        print(f"You got {percentage}% in This exam")
        send=Graph(math_Q,physic_Q,chemistry_Q,hindi_Q,english_Q,
        math_H=0,physic_H=0,chemistry_H=0,hindi_H=0,english_H=0,
        math_A=0,physic_A=0,chemistry_A=0,hindi_A=0,english_A=0)
        send.save_data()
        
        

class Quarterly: 

    def mathmatics():
        m=int(input("Enter Maths number: ") )   
        if m>=80:
            print("Wow, Congrates!!")
        return m

    def phys():
        p=int(input("Enter Physics number: "))
        if p>=80:
            print("Wow, Congrates!!")
        return p
    
    def chemis():
        c=int(input("Enter Chemistry number: "))
        if c>=80:
            print("Wow, Congrates!!")
        return c
    
    def hind():
        h=int(input("Enter Hindi number: "))
        if h>=80:
            print("Wow, Congrates!!")
        return h

    def engl():
        e=int(input("Enter English number: "))    
        if e>=80:
            print("Wow, Congrates!!")
        return e



class HalfYearly: 
    def mathmatics():
        m=int(input("Enter Maths number: ") )   
        if m>=80:
            print("Wow, Congrates!!")
        return m

    def phys():
        p=int(input("Enter Physics number: "))
        if p>=80:
            print("Wow, Congrates!!")
        return p
    
    def chemis():
        c=int(input("Enter Chemistry number: "))
        if c>=80:
            print("Wow, Congrates!!")
        return c
    
    def hind():
        h=int(input("Enter Hindi number: "))
        if h>=80:
            print("Wow, Congrates!!")
        return h

    def engl():
        e=int(input("Enter English number: "))    
        if e>=80:
            print("Wow, Congrates!!")
        return e



class Annual: 
    def mathmatics():
        m=int(input("Enter Maths number: ") )   
        if m>=80:
            print("Wow, Congrates!!")
        return m

    def phys():
        p=int(input("Enter Physics number: "))
        if p>=80:
            print("Wow, Congrates!!")
        return p
    
    def chemis():
        c=int(input("Enter Chemistry number: "))
        if c>=80:
            print("Wow, Congrates!!")
        return c
    
    def hind():
        h=int(input("Enter Hindi number: "))
        if h>=80:
            print("Wow, Congrates!!")
        return h

    def engl():
        e=int(input("Enter English number: "))    
        if e>=80:
            print("Wow, Congrates!!")
        return e





class Result(Quarterly,HalfYearly,Annual):
    
    def __init__(self,maths_q,phy_q,che_q,hin_q,eng_q,
                 maths_h,phy_h,che_h,hin_h,eng_h,
                 maths_a,phy_a,che_a,hin_a,eng_a,test_marks):
        
        self.math_q=maths_q
        self.math_a=maths_a
        self.math_h=maths_h
        self.phy_q=phy_q
        self.phy_h=phy_h
        self.phy_a=phy_a
        self.che_q=che_q
        self.che_h=che_h
        self.che_a=che_a
        self.hin_q=hin_q
        self.hin_h=hin_h
        self.hin_a=hin_a
        self.eng_q=eng_q
        self.eng_h=eng_h
        self.eng_a=eng_a
        self.test=test_marks
    
    def __str__(self) :
        Result.send_data('')
        
    
    def send_data(self):
        math_Q=self.math_q
        physic_Q=self.phy_q
        chemistry_Q=self.che_q
        hindi_Q=self.hin_q
        english_Q=self.eng_q
        math_H=self.math_h
        physic_H=self.phy_h
        chemistry_H=self.che_h
        hindi_H=self.hin_h
        english_H=self.eng_h
        math_A=self.math_a
        physic_A=self.phy_a
        chemistry_A=self.che_a
        hindi_A=self.hin_a
        english_A=self.eng_a
        
        test_marks=self.test
        
        if test_marks !=0:
            
            send= Graph(math_Q=math_Q,physic_Q=physic_Q,chemistry_Q=chemistry_Q,hindi_Q=hindi_Q,english_Q=english_Q,
                        math_H=math_H,physic_H=physic_H,chemistry_H=chemistry_H,hindi_H=hindi_H,english_H=english_H,
                        math_A=math_A,physic_A=physic_A,chemistry_A=chemistry_A,hindi_A=hindi_A,english_A=english_A,test=test_marks)
        else:
             send= Graph(math_Q=math_Q,physic_Q=physic_Q,chemistry_Q=chemistry_Q,hindi_Q=hindi_Q,english_Q=english_Q,
                        math_H=math_H,physic_H=physic_H,chemistry_H=chemistry_H,hindi_H=hindi_H,english_H=english_H,
                        math_A=math_A,physic_A=physic_A,chemistry_A=chemistry_A,hindi_A=hindi_A,english_A=english_A,test=0)
        send.save_data()
        
    
    def maths_res(self):
        math_Q=self.math_q
        math_H=self.math_h
        math_A=self.math_a
        total_M=math_Q+math_A+math_H
        
    def physics_res(self):
        physic_Q=self.phy_q
        physic_H=self.phy_h
        physic_A=self.phy_a
        total_P=physic_A+physic_H+physic_Q
        
    def chemsitry_res(self):
        chemistry_Q=self.che_q
        chemistry_H=self.che_h
        chemistry_A=self.che_a
        total_C=chemistry_A+chemistry_H+chemistry_Q

    def hindi_res(self):
        hindi_Q=self.hin_q
        hindi_H=self.hin_h
        hindi_A=self.hin_a
        total_H=hindi_H+hindi_A+hindi_Q
    def english_res(self):
        english_Q=self.eng_q
        english_H=self.eng_h
        english_A=self.eng_a
        total_E=english_A+english_H+english_Q
    
    def quarterly_res(self):
        math_Q=self.math_q
        physic_Q=self.phy_q
        chemistry_Q=self.che_q
        hindi_Q=self.hin_q
        english_Q=self.eng_q
        add_result=math_Q+physic_Q+chemistry_Q+hindi_Q+english_Q
        percentage=add_result/5
        total= f"{percentage}%"
        
    def Half_yearly_res(self):
        math_H=self.math_h
        physic_H=self.phy_h
        chemistry_H=self.che_h
        hindi_H=self.hin_h
        english_H=self.eng_h
        add_result=math_H+physic_H+chemistry_H+hindi_H+english_H
        percentage=add_result/5
        total=f"{percentage}%"

    def annual_res(self):
        math_A=self.math_a
        physic_A=self.phy_a
        chemistry_A=self.che_a
        hindi_A=self.hin_a
        english_A=self.eng_a
        add_result=math_A+physic_A+chemistry_A+hindi_A+english_A
        percentage=add_result/5
        total= f"{percentage}%"
        
    
    def test_res(self):
        test_t=self.test
        marks=0
        for i in range(len(test_t)):
            marks+=test_t[i]
        if marks!=0:
            print(int(marks))
   
def main():     
    try:
        star='*'
        print(star*56)
        print(star*20,"Fill From Here",star*20)
        print(star*56)


        name = input('Enter your name: ')
        phone = input("Enter 10-digit phone number: ")
        while len(phone) != 10:
            print(f"Phone number must be 10 digits long.\tYou Enterd {len(phone)}")
            phone = input("Enter phone number: ")
        manage=Manage(name,phone)
        manage.makefile()
        return exam_input()
    except Exception as e:
        print("Invalid",e)
        return main()       

        
def exam_input():

    try:
        which_exam=int(input("Enter 0 to calculate One Exam  or 1 for All('Quarterly/Halfyearly/Annual')"))
        if which_exam==0:
            maths_q=Quarterly.mathmatics()
            phy_q=Quarterly.phys()
            che_q=Quarterly.chemis()
            hin_q=Quarterly.hind()
            eng_q=Quarterly.engl()
            
            single_exam=Single_exam(maths=maths_q,phy=phy_q,
                                    chem=che_q,hin=hin_q,eng=eng_q)
            single_exam.single_exam()
            
            
        else:
        
        
            print("\n\n\n\nFill Quarterly Marks:\n")
            maths_q=Quarterly.mathmatics()
            phy_q=Quarterly.phys()
            che_q=Quarterly.chemis()
            hin_q=Quarterly.hind()
            eng_q=Quarterly.engl()


            print("\n\n\n\nFill Halfyearly Marks:\n")
            maths_h=HalfYearly.mathmatics()
            phy_h=HalfYearly.phys()
            che_h=HalfYearly.chemis()
            hin_h=HalfYearly.hind()
            eng_h=HalfYearly.engl()

            print("\n\n\n\nFill Annual Marks:\n")
            maths_a=Annual.mathmatics()
            phy_a=Annual.phys()
            che_a= Annual.chemis()
            hin_a=Annual.hind()
            eng_a=Annual.engl()
        
        
            yes_no=input("Do you want to add Test-marks  (y/n)?: ")
            cmd=yes_no.lower()
            test_marks=[]
            if cmd=='y':
                print("Enter marks (out of 100)\n")
                for i in range (5):
                    marks = int(input(f"{i+1} subject: "))
                    test_marks.append(marks)

            result=Result(maths_a=maths_a,maths_q=maths_q,maths_h=maths_h,
                phy_q=phy_q,phy_h=phy_h,phy_a=phy_a,
                che_q=che_q,che_h=che_h,che_a=che_a,
                hin_q=hin_q,hin_h=hin_h,hin_a=hin_a,
                eng_a=eng_a,eng_h=eng_h,eng_q=eng_q,test_marks=test_marks)
            
            # result.quarterly_res()
            # result.Half_yearly_res()
            # result.annual_res()
            # result.test_res()
            result.send_data()
            
            return result
            

    except Exception as e:
        print("Invalid",e)
        return exam_input()


main()


