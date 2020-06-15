import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("facebook-automation")
root.geometry('600x690')
root.configure(bg="#11E5DB")
root.resizable(0,0)
frame=Frame(root,height=30)
frame.pack(side=TOP)
lbl_title = Label(frame, text="Facebook-Automation", font="Arial 15 bold", bg="orange",  width = 300,fg="green")
lbl_title.pack(fill=X)
l1=Label(root,text="Username:-",bg="#11E5DB",fg="blue",font="Arial 15 bold")
l1.place(x=120,y=80)
user_field=Entry(root,width=40)
user_field.place(x=240,y=80)
l2=Label(root,text="password:-",bg="#11E5DB",fg="blue",font="Arial 15 bold")
l2.place(x=120,y=120)
passw_field=Entry(root,show="*",width=40)
passw_field.place(x=240,y=120)
l3=Label(root,text="Group-ids:-",bg="#11E5DB",fg="blue",font="Arial 15 bold")
l3.place(x=120,y=160)
msg=Text(root,height=10,width=40)
msg.place(x=240,y=160)
l4=Label(root,text="message:-",bg="#11E5DB",fg="blue",font="Arial 15 bold")
l4.place(x=120,y=360)
msg1=Text(root,height=10,width=40)
msg1.place(x=240,y=360)
l5=Label(root,fg="blue",bg="#11E5DB",font="Arial 15 bold")
l5.place(x=220,y=620)
def send():
    if(user_field.get()=='' or passw_field.get()=='' or  msg.get("1.0",END)=='' or  msg1.get('1.0',END)==''):
            messagebox.showinfo("information","fill the details")  
    else:
        m=[]
        l=msg.get("1.0",END)
        print(l)
        m=l.split(",")
        s=m[-1]
        s=s[1:-1]
        m[-1]=s
        print(m)
        options = Options()
        options.add_argument("--disable-notifications")
        driver=webdriver.Chrome(executable_path='/usr/bin/chromedriver')    
        driver.get('https://www.facebook.com/')
        time.sleep(10)
        while(True):
            try:
                driver.maximize_window()
                time.sleep(5)
                driver.find_element_by_id('email').click()
                driver.find_element_by_id('email').send_keys(user_field.get())
                driver.find_element_by_id('pass').click()
                driver.find_element_by_id('pass').send_keys(passw_field.get())
                driver.find_element_by_id('pass').send_keys(Keys.ENTER)
                break
            except:
                pass
        time.sleep(5)
        i=0
        while(i<len(m)):
            try:
                driver.get('https://www.facebook.com/groups/%s'%(m[i]))
                time.sleep(10)
                Element=driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[3]/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[1]/div/div/div[1]/div")
                Element.click()
                time.sleep(5)
                pyautogui.typewrite(msg1.get("1.0",END))
                print("post writing was completed")
                root.update()
                time.sleep(5)
                button=driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[4]/div/div/div[1]/div/form/div/div/div/div/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div")
                button.click()
                print("post was done in %s"%(m[i]))
                root.update()
                l5.configure(text="%d/%d completed"%(i+1,len(m)))
                time.sleep(5)
                i+=1
            except:
                i+=1
                pass
def clear():
    l5.configure(text="")
    user_field.delete(first=0,last=100)
    passw_field.delete(first=0,last=100)
    msg.delete('1.0',END)
    msg1.delete('1.0',END)
b1=Button(root,text="send",bg="pink",font="Arial 15 bold",activebackground="pink",command=send)
b1.place(x=250,y=550)
b2=Button(root,text="clear",bg="pink",font="Arial 15 bold",activebackground="pink",command=clear)
b2.place(x=360,y=550)
root.mainloop()
