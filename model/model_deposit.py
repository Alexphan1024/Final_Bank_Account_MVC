from model.model_readcsv import *
from model.model_logs import *
from tkinter import messagebox
import os

class Model_Deposit:
    def __init__(self, master, paypage,acc_id,acc_type):
        self.master= master
        self.paypage= paypage
        self.r = Read_csv()
        self.r.readcsv()
        self.info = self.r.infomation
        self.log = Log()
        self.id = acc_id
        self.type = acc_type

    def deposit(self,num):
        mess = "Deposit ${}".format(num)
        self.master.withdraw()
        messagebox.showinfo(title="Deposit", message=mess)
        self.paypage.deiconify()
        self.log.adds(str(self.id), "Deposit $ ", str(num),self.type)
        self.info[self.r.search_acc_id(self.id)[0]][int(self.type)] = int(self.info[self.r.search_acc_id(self.id)[0]][int(self.type)]) + num
        with open(os.path.dirname(__file__) + '\\info.csv', 'w+') as updated:
            csv_writer = csv.writer(updated, lineterminator='\n')
            csv_writer.writerow(("Name","ID","Pin","cBalance","sBalance","Log"))
            for rows in self.info:
                csv_writer.writerow(rows)
