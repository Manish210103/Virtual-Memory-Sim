import tkinter as tk

import random as rd

root = tk.Tk()


num_process_var=tk.StringVar()
log_add_input=tk.StringVar()
submit_flag=0
index=0

class Table:
    def __init__(self, root, rows, columns, row_start, column_start, bg_color="black", fg_color="black"):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.row_start = row_start
        self.column_start = column_start
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.table = [[None for j in range(columns)] for i in range(rows)]

        for i in range(rows):
            for j in range(columns):
                entry = tk.Entry(root, width=10, bg=bg_color, fg=fg_color)
                entry.grid(row=i + row_start, column=j*2 + column_start)
                self.table[i][j] = entry
        
    def get_values(self):
        return [[self.table[i][j].get() for j in range(self.columns)] for i in range(self.rows)]

    def put_values(self):
        num_rows = self.rows-20
        num_cols = self.columns
        values = []
        for i in range(num_rows):
            j = i + 1
            value_str = '0x{:04X}'.format(j)
            #self.table[i][j].insert(i,value_str)
            values.append(value_str)
        #print(values)
        k=0
        self.table[0][0].insert(0,"Frame_no")
        self.table[0][1].insert(0,"Values")
        for i in range(1,num_rows):
            self.table[i][0].insert(i,values[k])
            k+=1
        with open('input.txt','r') as file:
            lines= [line.strip() for line in file.readlines()]
           
        rd.shuffle(lines)
         
        k=0
        for i in range(1,len(lines)+1):
            self.table[i][1].insert(i,lines[k])
            k+=1
            
       
        return values

           
    def put_pg_table_values(self,sec_mem_values,main_mem_values):
        #print(sec_mem_values)
        rd.shuffle(sec_mem_values)
        list1=[]  
        p_bit=[]
        #print(sec_mem_values)
        k=0
        self.table[0][0].insert(0,"Page_No")
        for i in range(1,self.rows-2):
            self.table[i][0].insert(i,sec_mem_values[k])
            list1.append(sec_mem_values[k])
            sec_mem_values.remove(sec_mem_values[k])
            k=k+1
        self.table[i+1][0].insert(i,"0x00D4")
        list1.append("0x00D4")
        self.table[i+2][0].insert(i,"0x00D9")
        list1.append("0x00D9")
       
        k=0
        self.table[0][1].insert(0,"Frame_no")
        frames=[]
        for i in range(1,self.rows-2):
            self.table[i][1].insert(i,sec_mem_values[k])
            frames.append(sec_mem_values[k])
            sec_mem_values.remove(sec_mem_values[k])
            k=k+1
        self.table[i+1][1].insert(i,"0x0013")
        frames.append("0x0013")
        self.table[i+2][1].insert(i,"0x0014")
        frames.append("0x0014")
           
       
        i=1
        self.table[0][2].insert(0,"Present_Bit")
        for values in frames:
            if i<self.rows-2:
            #print(values)
                if values in main_mem_values:
                    self.table[i][2].insert(i,1)
                    p_bit.append(1)
                else:
                    self.table[i][2].insert(i,0)
                    p_bit.append(0)
                i+=1
        self.table[i][2].insert(0,0)
        p_bit.append(0)
        self.table[i+1][2].insert(0,1)
        p_bit.append(1)
           
        result = [[list1[i], frames[i], p_bit[i]] for i in range(len(list1))]
        return result
       
       
           
       
           
    def put_tlb_values(self,tot_pg_table_vals):
        tlb_val1=[]
        tlb_val2=[]
        #print(tot_pg_table_vals)
        rd.shuffle(tot_pg_table_vals)
        k=0
        global index
        index=rd.randint(1,self.rows-2)
        print(index)
        self.table[0][0].insert(0,"Page_No")
        self.table[0][1].insert(0,"PT_entry")
        for i in range(1,index+1):
            self.table[i][0].insert(i,tot_pg_table_vals[k][0])
            self.table[i][1].insert(i,tot_pg_table_vals[k][1])
            tlb_val1.append(tot_pg_table_vals[k][0])
            tlb_val2.append(tot_pg_table_vals[k][1])
            tot_pg_table_vals.remove(tot_pg_table_vals[k])
            k=k+1
        self.table[i+1][0].insert(i,"0x00A0")
        self.table[i+1][1].insert(i,"0x0011")
        tlb_val1.append("0x00A0")
        tlb_val2.append("0x0011")
        result = [[tlb_val1[i], tlb_val2[i]] for i in range(len(tlb_val1))]
        return result

    def put_values_logi(self):
        self.table[0][0].insert(0,"Page No")
        self.table[0][1].insert(0,"Offset")
        log_add_input1=log_add_input.get()
        page_no=log_add_input1[0:6]
        offset=log_add_input1[6:9]
        self.table[1][0].insert(0,page_no)
        self.table[1][1].insert(0,offset)
   
    def put_pa_values_basic(self):
        self.table[0][0].insert(0,"Frame_no")
        self.table[0][1].insert(0,"Offset")
        log_add_input1=log_add_input.get()
        offset=log_add_input1[6:9]
        self.table[1][1].insert(0,offset)

       
    def put_pa_values(self,val):
        self.table[0][0].insert(0,"Frame_no")
        self.table[0][1].insert(0,"Offset")
        log_add_input1=log_add_input.get()
        page_no=log_add_input1[0:6]
        offset=log_add_input1[6:9]
        self.table[1][1].insert(0,offset)
        self.table[1][0].insert(0,val)
   
    def put_frame_no_and_val(self,frame_no_and_val):
        for i in range(self.rows):
            if self.table[i][0]=="":
                self.table[i][0].insert(0,frame_no_and_val[0])
                self.table[i][1].insert(0,frame_no_and_val[1])
   
    def put_tlb_page_no_and_frame_no(self,page_no,frame_no):
        count=0
        global index
        if index+3!=self.rows:
            self.table[index+2][0].insert(0,page_no+"-u")
            self.table[index+2][1].insert(0,frame_no+"-u")
        else:
            self.table[1][0].delete(0,6)
            self.table[1][1].delete(0,6)
            self.table[1][0].insert(0,page_no+"-u")
            self.table[1][1].insert(1,frame_no+"-u")                
       
       
def check_pgtble_hitmiss(tot_pg_table_vals,page_no):
    flag=0
    pgtble_hit=""
    pgtble_miss=""
    print(tot_pg_table_vals[0][2])
    for i in range(len(tot_pg_table_vals)):
        if page_no in tot_pg_table_vals[i][0] and tot_pg_table_vals[i][2]==1:
            print("page table hit")
            flag=1
            break
        elif page_no in tot_pg_table_vals[i][0] and tot_pg_table_vals[i][2]==0:
            pgtble_miss=tot_pg_table_vals[i][1]
            print("page table miss")
            flag=0
            break
        else:
            flag=2
            print("page not in memory")
    if(flag==0):

        popup = tk.Toplevel(root)
        # set the title of the pop-up window
        popup.title("New Pop-up Window")
               
        # set the size of the pop-up window
        popup.configure(bg="black")
        popup.geometry("150x100")
        popup.geometry("+{x}+{y}".format(x=650, y=300))

        # create a label in the pop-up window
        label = tk.Label(popup, text="PAGE FAULT",bg='black',fg='red')
        label.pack(padx=20, pady=20)
    elif flag==1:
        popup = tk.Toplevel(root)
        pgtble_hit=tot_pg_table_vals[i][1]

        # set the title of the pop-up window
        popup.title("New Pop-up Window")
   
        # set the size of the pop-up window
        popup.configure(bg="black")
        popup.geometry("150x100")
        popup.geometry("+{x}+{y}".format(x=650, y=300))

        # create a label in the pop-up window
        label = tk.Label(popup, text="PAGE TABLE HIT",bg='black',fg='red')
        label.pack(padx=20, pady=20)
       
    elif flag==2:
        popup = tk.Toplevel(root)
        # set the title of the pop-up window
        popup.title("New Pop-up Window")
               
        # set the size of the pop-up window
        popup.configure(bg="black")
        popup.geometry("200x100")
        popup.geometry("+{x}+{y}".format(x=600, y=300))

        # create a label in the pop-up window
        label = tk.Label(popup, text="PAGE NOT IN MEMORY",bg='black',fg='red')
        label.pack(padx=20, pady=20)
    val=[pgtble_hit,pgtble_miss]  
    return val
           
def check_tlb_hitmiss(tlb_val,page_no,tot_pg_table_vals):
    flag=0
    tlb_vals=""
    pgtble_val=["",""]
    for i in range(len(tlb_val)):
        if page_no in tlb_val[i][0]:
            popup = tk.Toplevel(root)
            tlb_vals=tlb_val[i][1]

        # set the title of the pop-up window
            popup.title("New Pop-up Window")
       
            # set the size of the pop-up window
            popup.configure(bg="black")
            popup.geometry("100x100")
            popup.geometry("+{x}+{y}".format(x=700, y=300))

            # create a label in the pop-up window
            label = tk.Label(popup, text="TLB HIT",bg='black',fg='red')
            label.pack(padx=20, pady=20)
            flag=1
            print("HIT")
        else:
            print("MISS")
    if flag==0:
        pgtble_val=check_pgtble_hitmiss(tot_pg_table_vals,page_no)
    vals=[tlb_vals,pgtble_val[0],pgtble_val[1]]
    return vals

def check_sec_mem(frame_no,sec_mem_values):
    frame_no_and_val=""
    for i in range(len(sec_mem_values)):
        if frame_no in sec_mem_values[i][0]:
            frame_no_and_val=[frame_no,sec_mem_values[i][1]]
           
    return frame_no_and_val

def submit1():
    num=num_process_var.get()
    #print(num)
    num=int(num)
    print("Number of processes:",num)
    #print("Type:",type(num))
    pg_tables=[]
    y=9
    x=25
    table1 = Table(root, 2, 2, 10, 3, "black", "red") #logical address
    table2 = Table(root, 16, 2, 5, 9, "black", "red") #tlb
    for i in range(num):
        pg_table=Table(root, 16, 3, x, y, "black", "red") #page table
        tk.Label(root, text="", bg="black").grid(row=0, column=y-3)
        pg_tables.append(pg_table)
        y=y+10
   
    table4 = Table(root, 2, 2, 10, y, "black", "red") #physical address
   
    tk.Label(root, text="", bg="black").grid(row=0, column=y+4)
    table5 = Table(root, 100, 2, 5, y+10, "black", "red")  #main memory
    tk.Label(root, text="", bg="black").grid(row=0, column=y+18)
   
    table6 = Table(root, 256, 2, 5, y+20, "black", "red")  #secondary memory
   
    main_mem_values=table5.put_values()
    sec_mem_values=table6.put_values()
    log_add_input1=log_add_input.get()
    page_no=log_add_input1[0:6]


    tot_pg_table_vals=[]
    tot_pg_table_frames=[]
    for table in pg_tables:
        table_val=[]
        table_val=table.put_pg_table_values(sec_mem_values,main_mem_values)
        print("\n\nhello\n\n")
        #print(table_val)
        for val in table_val:
            tot_pg_table_vals.append(val)
   
    print(tot_pg_table_vals)
    tlb_val=table2.put_tlb_values(tot_pg_table_vals)
    table1.put_values_logi()#adding the values into the logical address table
   
    vals=check_tlb_hitmiss(tlb_val,page_no,tot_pg_table_vals)
    print(vals)
    if vals[0]=="" and vals[2]=="":
        table4.put_pa_values(vals[1])
    elif vals[1]=="" and vals[2]=="":
        table4.put_pa_values(vals[0])
    elif vals[0]=="" and vals[1]=="":
        table4.put_pa_values_basic()
        frame_no_and_val=check_sec_mem(vals[2],sec_mem_values)
        table5.put_frame_no_and_val(frame_no_and_val)
        table2.put_tlb_page_no_and_frame_no(page_no,vals[2])
   

   
   
if __name__ == '__main__':
    root.configure(bg="black")
    root.geometry("800x500")    
   
    #number of processes -> entry widget
    tk.Label(root, text="Processes",bg="black",fg="white").grid(row=0,column=0)
    num_process = tk.Entry(root,textvariable = num_process_var, font=('calibre',8,'normal'))
    num_process.grid(row=0,column=1)
    #logical address -> entry widget
    tk.Label(root,text="Logical address", bg="black", fg="white").grid(row=2,column=0)
    logi=tk.Entry(root,textvariable=log_add_input,font=('calibre',8,'normal') )
    logi.grid(row=2,column=1)
    #submit button
    sub_btn1=tk.Button(root,text="submit",command=submit1)
    sub_btn1.grid(row=3,column=0)


    # add empty Labels to create spaces between tables

    tk.Label(root, text="", bg="black").grid(row=0, column=6)
    tk.Label(root, text="", bg="black").grid(row=0, column=19)
    tk.Label(root, text="", bg="black").grid(row=25, column=5)


   

    root.mainloop()