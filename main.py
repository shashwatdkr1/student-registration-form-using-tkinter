from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
master = Tk()
master.configure(bg=&#39;#8533ff&#39;)
master.title(&#39;tk&#39;)
master.geometry(&#39;1000x5000&#39;)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;, text=&#39;First Name
&#39;).grid(row=0)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;(max 30 chracters a-z
and AZ)&#39;).grid(row=0,column=2)
Label(master, bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Last Name&#39;).grid(row=1)
Label(master, bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;(max 30 chracters a-z
and AZ)&#39;).grid(row=1,column=2)
Label(master, bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Date of
birth&#39;).grid(row=2)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;Email ID &#39;).grid(row=3)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;Mobile
Number&#39;).grid(row=4)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;(10 digit
number)&#39;).grid(row=4,column=2)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;Gender &#39;).grid(row=5)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;Address &#39;).grid(row=6)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;City &#39;).grid(row=7)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;(max 30 chracters a-z
and AZ)&#39;).grid(row=7,column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Pincode&#39;).grid(row=8)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;(6 digit
number)&#39;).grid(row=8,column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;State&#39;).grid(row=9)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;(max 30 chracters a-z and
AZ)&#39;).grid(row=9,column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Country&#39;).grid(row=10)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Hobbies&#39;).grid(row=11)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Qualification)&#39;).grid(row
=12)

Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Sl.No&#39;).grid(row=12,colum
n=1)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Examination&#39;).grid(row=12
,column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Board&#39;).grid(row=12,colum
n=3)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Percentage&#39;).grid(row=12,
column=4)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;YearofPassing&#39;).grid(row=
12,column=5)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;1&#39;).grid(row=13,column=1)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&#39;2&#39;).grid(row=14,column=1)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&#39;3&#39;).grid(row=15,column=1)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&#39;4&#39;).grid(row=16,column=1)
Label(master, bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Class
X&#39;).grid(row=13,column=2)
Label(master,bg=&#39;#8533ff&#39;, fg=&#39;white&#39;,text=&#39;Class
XII&#39;).grid(row=14,column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&#39;Graduation&#39;).grid(row=15,
column=2)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&#39;Masters&#39;).grid(row=16,column=2)
# Label(master, text= &quot;Day:&quot;).grid(row=2,column=1)
Label(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;, text=&#39;Courses
Applied&#39;).grid(row=17)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e13= Entry(master)
e14= Entry(master)
e15= Entry(master)
e16= Entry(master)
e17= Entry(master)
e18= Entry(master)
e19= Entry(master)
e20= Entry(master)
e21= Entry(master)
e22= Entry(master)
e23= Entry(master)
e24= Entry(master)
e1.grid(row=0, column=1,ipadx=30)

e2.grid(row=1, column=1,ipadx=30)
e3.grid(row=3,column=1,ipadx=30)
e4.grid(row=4,column=1,ipadx=30)
e5.grid(row=6,column=1,ipadx=30,ipady=30)
e6.grid(row=7,column=1,ipadx=30)
e7.grid(row=8,column=1,ipadx=30)
e8.grid(row=9,column=1,ipadx=30)
e9.grid(row=10,column=1,ipadx=30)
e13.grid(row=13,column=3,ipadx=30)
e14.grid(row=14,column=3,ipadx=30)
e15.grid(row=15,column=3,ipadx=30)
e16.grid(row=16,column=3,ipadx=30)
e17.grid(row=13,column=4,ipadx=30)
e18.grid(row=14,column=4,ipadx=30)
e19.grid(row=15,column=4,ipadx=30)
e20.grid(row=16,column=4,ipadx=30)
e21.grid(row=13,column=5,ipadx=30)
e22.grid(row=14,column=5,ipadx=30)
e23.grid(row=15,column=5,ipadx=30)
e24.grid(row=16,column=5,ipadx=30)
var1 = IntVar()
Radiobutton(master,bg=&#39;#8533ff&#39;,
fg=&#39;white&#39;,text=&quot;Male&quot;,variable=var1).grid(row=5, column=1,
sticky=W,ipady=10,ipadx=30)
var2 = IntVar()
Radiobutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&quot;Female&quot;,
variable=var2).grid(row=5, column=2, sticky=W,ipady=10,ipadx=10)
var3 = IntVar()
Checkbutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&quot;Drawing&quot;,variable=var3).grid(row=11,
column=1,sticky=W,ipady=10,ipadx=30)
var4 = IntVar()
Checkbutton(master,bg=&#39;#8533ff&#39;,
fg=&#39;white&#39;,text=&quot;Singing&quot;,variable=var4).grid(row=11, column=2,
sticky=W,ipady=10,ipadx=10)
var5 = IntVar()
Checkbutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&quot;Dancing&quot;,variable=v
ar5).grid(row=11, column=3, sticky=W,ipady=10,ipadx=30)
var6 = IntVar()
Checkbutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,
text=&quot;Sketching&quot;,variable=var6).grid(row=11, column=4,
sticky=W,ipady=10,ipadx=10)
var7 = IntVar()
Radiobutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&quot;BCA&quot;,variable=var7)
.grid(row=17, column=1,sticky=W,ipady=10,ipadx=30)
var8 = IntVar()
Radiobutton(master,
bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&quot;B.Com&quot;,variable=var8).grid(row=17,
column=2, sticky=W,ipady=10,ipadx=10)
var9 = IntVar()
Radiobutton(master,bg=&#39;#8533ff&#39;,fg=&#39;white&#39;,text=&quot;B.Sc&quot;,variable=var9
).grid(row=17, column=3,sticky=W,ipady=10,ipadx=30)
var10 = IntVar()
Radiobutton(master,bg=&#39;#8533ff&#39;,
fg=&#39;white&#39;,text=&quot;B.A&quot;,variable=var10).grid(row=17, column=4,
sticky=W,ipady=10,ipadx=10)

n = tk.StringVar()
p = tk.StringVar()
q = tk.StringVar()
monthchoosen = ttk.Combobox(master, width = 27, textvariable = n)
datechosen = ttk.Combobox(master, width = 27, textvariable = p)
yearchosen = ttk.Combobox(master, width = 27, textvariable = q)
datechosen[&#39;values&#39;]=(&quot;1&quot;,
&quot;2&quot;,
&quot;3&quot;,
&quot;4&quot;,
&quot;5&quot;)
monthchoosen[&#39;values&#39;] = (&#39; January&#39;,
&#39; February&#39;,
&#39; March&#39;,
&#39; April&#39;,
&#39; May&#39;,
&#39; June&#39;,
&#39; July&#39;,
&#39; August&#39;,
&#39; September&#39;,
&#39; October&#39;,
&#39; November&#39;,
&#39; December&#39;)
yearchosen[&#39;values&#39;]=(&quot;2001&quot;,
&quot;2002&quot;,
&quot;2003&quot;,
&quot;2004&quot;)
datechosen.grid(column=1,row=2)
datechosen.set(&quot;Date&quot;)
monthchoosen.grid(column = 2, row = 2)
monthchoosen.set(&quot;Month&quot;)
yearchosen.grid(column = 3, row = 2)
yearchosen.set(&quot;Year&quot;)
btn = Button(master, text=&#39;Submit&#39;).grid(row=18,column=2)
btn = Button(master, text=&#39;Reset&#39;).grid(row=18, column=3)
master.mainloop()