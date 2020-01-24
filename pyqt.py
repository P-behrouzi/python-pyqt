
import json
import sys

import requests
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from idna.core import unicode

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 450
        self.top = 200
        self.width = 500
        self.height = 500
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        loop=0
        while(loop!=1):
            key=self.get_username()
            if(key!=None):
                loop=1
                self.my_menu(key)
            else:
                loop+=2
            if(loop==6):
                break
        self.show()
    
    def get_username(self):
        user,okPressed=QInputDialog.getText(self,"username","deful username:test", QLineEdit.Normal, "")
        if okPressed:
            pas,okPressed=QInputDialog.getText(self,"password","default password: test", QLineEdit.Password, "")
            if okPressed: 
                inputt={"username":user ,"password":pas }
                re=requests.post("http://176.9.164.222:2211/api/Login",data=inputt)
                try:
                    re=re.text
                    re=json.loads(re)
                    re=re["token"]
                    if 're' in locals():
                        msg=QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setDetailedText("access account success")
                        msg.exec_()
                        return re
                except KeyError as re:
                    msg=QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("user or password is wrong")
                    msg.exec_()

    def my_menu(self,key):
        button1=QPushButton("show all account",self)
        button1.move(50,10)
        button1.resize(200,40)
        button1.setStyleSheet("background-color: green")
        button1.clicked.connect(lambda:self.all_account(key))
        button2=QPushButton("add account",self)
        button2.move(270,10)
        button2.resize(200,40)
        button2.setStyleSheet("background-color: orange")
        button2.clicked.connect(lambda:self.add_account(key))
        button3=QPushButton("sign up",self)
        button3.move(50,60)
        button3.resize(200,40)
        button3.setStyleSheet("background-color: blue")
        button3.clicked.connect(lambda:self.sign_up(key))
        button4=QPushButton("show log special account",self)
        button4.move(270,60)
        button4.resize(200,40)
        button4.setStyleSheet("background-color: yellow")
        button4.clicked.connect(lambda:self.log_account(key))
        button5=QPushButton("close account",self)
        button5.move(50,110)
        button5.resize(200,40)
        button5.setStyleSheet("background-color: gray")
        button5.clicked.connect(lambda:self.close_account(key))
        button6=QPushButton("block account",self)
        button6.move(270,110)
        button6.resize(200,40)
        button6.setStyleSheet("background-color: black")
        button6.clicked.connect(lambda:self.block_account(key))
        button7=QPushButton("retrieve normall account",self)
        button7.move(50,170)
        button7.resize(200,40)
        button7.setStyleSheet("background-color: white")
        button7.clicked.connect(lambda:self.retn_account(key))
        button8=QPushButton("retrieve owner account",self)
        button8.move(270,170)
        button8.resize(200,40)
        button8.setStyleSheet("background-color: pink")
        button8.clicked.connect(lambda:self.reto_account(key))
        button9=QPushButton("card to card",self)
        button9.move(50,230)
        button9.resize(200,40)
        button9.setStyleSheet("background-color: purple")
        button9.clicked.connect(lambda:self.card_to_card(key))
        button10=QPushButton("discharge account",self)
        button10.move(270,230)
        button10.resize(200,40)
        button10.setStyleSheet("background-color: red")
        button10.clicked.connect(lambda:self.charge_account(key))
        button11=QPushButton("charge account",self)
        button11.move(50,290)
        button11.resize(200,40)
        button11.setStyleSheet("background-color: brown")
        button11.clicked.connect(lambda:self.discharge_account(key))
        button12=QPushButton("show all translate",self)
        button12.move(270,290)
        button12.resize(200,40)
        button12.setStyleSheet("background-color: olive")
        button12.clicked.connect(lambda:self.all_translate(key))



    @pyqtSlot()

    def all_translate(self,key):
        my_list=requests.get("http://176.9.164.222:2211/api/transaction/TransactionListCreate"
        ,headers={'Authorization': 'JWT ' + key})
        my_list=my_list.text                
        my_list=json.loads(my_list)
        msgbox = QMessageBox()
        msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
        msgbox.setWindowTitle("translate")
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setText("see detail for all translate ")
        msgbox.setDetailedText( "%s\n" % my_list)
        msgbox.exec_()


    def discharge_account(self,key):
        fromm,okpressed=QInputDialog.getText(self,"account","your account",QLineEdit.Normal,"")
        if okpressed:
            amount,okpressed=QInputDialog.getInt(self,"amont","how much to discharge:",0,1,1000,1)
            if okpressed:
                inputt={"fromAccount":None,"toAccount":fromm,"amount":amount,"definition":"",'cash':True}
                my_list=requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",data=inputt
                ,headers={'Authorization': 'JWT ' + key})
                my_list=my_list.text                
                my_list=json.loads(my_list)
                msgbox = QMessageBox()
                msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
                msgbox.setWindowTitle("discharge")
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("see detail for success or not ")
                msgbox.setDetailedText( "%s\n" % my_list)
                msgbox.exec_()


    def charge_account(self,key):
        fromm,okpressed=QInputDialog.getText(self,"account","your account",QLineEdit.Normal,"")
        if okpressed:
            amount,okpressed=QInputDialog.getInt(self,"amont","how much to charge:",0,1,1000,1)
            if okpressed:
                inputt={"fromAccount":fromm,"toAccount":None,"amount":amount,"definition":"",'cash':True}
                my_list=requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",data=inputt
                ,headers={'Authorization': 'JWT ' + key})
                my_list=my_list.text                
                my_list=json.loads(my_list)
                msgbox = QMessageBox()
                msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
                msgbox.setWindowTitle("charge")
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("see detail for success or not ")
                msgbox.setDetailedText( "%s\n" % my_list)
                msgbox.exec_()


    def card_to_card(self,key):
        fromm,okpressed=QInputDialog.getText(self,"account","origin account",QLineEdit.Normal,"")
        if okpressed:
            to,okpressed=QInputDialog.getText(self,"account","purpose account",QLineEdit.Normal,"")
            if okpressed:
                amount,okpressed=QInputDialog.getInt(self,"amont","how much to translate:",0,1,1000,1)
                if okpressed:
                    inputt={"fromAccount":fromm,"toAccount":to,"amount":amount,"definition":"",'cash':False}
                    my_list=requests.post("http://176.9.164.222:2211/api/transaction/TransactionListCreate",data=inputt
                    ,headers={'Authorization': 'JWT ' + key})
                    my_list=my_list.text                
                    my_list=json.loads(my_list)
                    msgbox = QMessageBox()
                    msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
                    msgbox.setWindowTitle("card to card")
                    msgbox.setIcon(QMessageBox.Information)
                    msgbox.setText("see detail for success or not ")
                    msgbox.setDetailedText( "%s\n" % my_list)
                    msgbox.exec_()

    def reto_account(self,key):
        number,okpressed=QInputDialog.getText(self,"national code","your national code",QLineEdit.Normal,"")
        if okpressed:
            url="http://176.9.164.222:2211/api/accounts/AccountOwnerRetrieve/"
            url+=number
            my_list=requests.get(url,headers={'Authorization': 'JWT ' + key})
            my_list=my_list.text                
            my_list=json.loads(my_list)
            msgbox = QMessageBox()
            msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
            msgbox.setWindowTitle("retrieve account")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("see detail for success or not ")
            msgbox.setDetailedText( "%s\n" % my_list)
            msgbox.exec_()


    def retn_account(self,key):
        number,okpressed=QInputDialog.getText(self,"account number","your account number",QLineEdit.Normal,"")
        if okpressed:
            url="http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/"
            url+=number
            my_list=requests.get(url,headers={'Authorization': 'JWT ' + key})
            my_list=my_list.text                
            my_list=json.loads(my_list)
            msgbox = QMessageBox()
            msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
            msgbox.setWindowTitle("retrieve account")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("see detail for success or not ")
            msgbox.setDetailedText( "%s\n" % my_list)
            msgbox.exec_()

    def block_account(self,key):
        number,okpressed=QInputDialog.getText(self,"account number","your account number",QLineEdit.Normal,"")
        if okpressed:
            inputt={"accountNumber":number}
            my_list=requests.post("http://176.9.164.222:2211/api/accounts/BlockAccount",json=inputt
            ,headers={'Authorization': 'JWT ' + key})
            my_list=my_list.text                
            my_list=json.loads(my_list)
            msgbox = QMessageBox()
            msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
            msgbox.setWindowTitle("block account")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("see detail for success or not ")
            msgbox.setDetailedText( "%s\n" % my_list)
            msgbox.exec_()

    def close_account(self,key):
        number,okpressed=QInputDialog.getText(self,"account number","your account number",QLineEdit.Normal,"")
        if okpressed:
            inputt={"accountNumber":number}
            my_list=requests.post("http://176.9.164.222:2211/api/accounts/CloseAccount",json=inputt
            ,headers={'Authorization': 'JWT ' + key})
            my_list=my_list.text                
            my_list=json.loads(my_list)
            msgbox = QMessageBox()
            msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
            msgbox.setWindowTitle("close account")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("see detail for success or not ")
            msgbox.setDetailedText( "%s\n" % my_list)
            msgbox.exec_()

    def log_account(self,key):
        number,okpressed=QInputDialog.getText(self,"account number","your account number",QLineEdit.Normal,"")
        if okpressed:
            inputt={"accountNumber":number}
            my_list=requests.post("http://176.9.164.222:2211/api/accounts/GetBankAccountLogs",json=inputt
            ,headers={'Authorization': 'JWT ' + key})
            my_list=my_list.text                
            my_list=json.loads(my_list)
            msgbox = QMessageBox()
            msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
            msgbox.setWindowTitle("log account")
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("your log")
            msgbox.setDetailedText( "%s\n" % my_list)
            msgbox.exec_()

    def sign_up(self,key):
        user,okpressed=QInputDialog.getText(self,"username","your user",QLineEdit.Normal,"")
        if okpressed:
            pas,okPressed=QInputDialog.getText(self,"password","your password",QLineEdit.Password,"")
            if okpressed:
                inputt={"username":user,"password":pas }
                my_list=requests.post("http://176.9.164.222:2211/api/accounts/User/SignUp",json=inputt
                ,headers={'Authorization': 'JWT ' + key})
                my_list=my_list.text                
                my_list=json.loads(my_list)
            if(my_list['username']==['A user with that username already exists.']):
                msgbox = QMessageBox()
                msgbox.setStyleSheet("QLabel{min-width: 100px;min-height:50px}")
                msgbox.setWindowTitle("sign up")
                msgbox.setIcon(QMessageBox.Critical)
                msgbox.setText("sign up faild")
                msgbox.exec_()
            else:
                msgbox = QMessageBox()
                msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
                msgbox.setWindowTitle("sign up")
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("sign up success")
                msgbox.setDetailedText( "%s\n" % my_list)
                msgbox.exec_()
    def add_account(self,key):
        user,okPressed=QInputDialog.getText(self,"firstname","your firstname", QLineEdit.Normal, "")
        if okPressed:
            pas,okPressed=QInputDialog.getText(self,"lastname","your lastname", QLineEdit.Password, "")
            if okPressed:
                phone,okPressed=QInputDialog.getText(self,"phone number","your phone", QLineEdit.Normal, "")
                if okPressed:
                    national,okPressed=QInputDialog.getText(self,"nationalcode","your nationalcode", QLineEdit.Normal, "")
                    if okPressed:
                        inputt={"accountOwner":{"firstName":user,"lastName":pas,"phoneNumber":phone,"nationalCode":national}}
                        my_list=requests.post("http://176.9.164.222:2211/api/accounts/BankAccountListCreate",json=inputt
                        ,headers={'Authorization': 'JWT ' + key})
                        my_list=my_list.text
                        my_list=json.loads(my_list)
                        msgbox = QMessageBox()
                        msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
                        msgbox.setWindowTitle("add account")
                        msgbox.setIcon(QMessageBox.Information)
                        msgbox.setDetailedText( "%s\n" % my_list)
                        msgbox.exec_()


    def all_account(self,key):
        my_list=requests.get("http://176.9.164.222:2211/api/accounts/BankAccountListCreate",
        headers={'Authorization': 'JWT ' + key})
        my_list=my_list.text
        my_list=json.loads(my_list)
        msgbox = QMessageBox()
        msgbox.setStyleSheet("QLabel{min-width: 700px;min-height:100px}")
        msgbox.setWindowTitle("all account in bank")
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setDetailedText( "%s\n" % my_list)
        msgbox.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
