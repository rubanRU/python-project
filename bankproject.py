import cx_Oracle
import random
class account(object):
    def acc(self):
        global val
        global val1
        global amo
        global typ
        global pas
        print(" ")
        print("ENTER THE FIRST NAME OF CUSTOMER")
        self.d1=str(input())
        print("")
        print("ENTER THE LAST NAME OF CUSTOMER")
        self.d2=str(input())
        print("")
        print("ENTER THE ADDRESS OF CUSTOMER")
        self.d3=str(input())
        print("")
        print("ENTER THE CITY OF CUSTOMER ")
        self.d4=str(input())
        print("")
        print("ENTER THE STATE OF CUSTOMER")
        self.d5=str(input())
        print("ENTER THE PINCODE")
        self.d6=int(input())
        print(" ")
        print("ENTER YOUR ACCOUNT TYPE --")
        print("1-Current")
        print("2-Savings")
        yy=str(input())
        if yy=="1":
            print(" ")
            print("YOUR ACCOUNT NUMBER IS :")
            val=random.randint(11111111,55555555)
            print(val)
            print(" ")
            print("YOUR CUSTOMER ID IS  :")
            val1=random.randint(11111111,55555555)
            print(val1)
            amo=1000
            typ="CURRENT"
            print(" ")
            print("SET PASSWORD FOR YOUR ACCOUNT!!!!!!!!!")
            pas=str(input())
            con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
            cur=con.cursor()
            sql = "insert into acco VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.d1,self.d2,self.d3,self.d4,self.d5,self.d6,val,val1,amo,typ,pas)
            cur.execute(sql)
            con.commit()
            print(" ")
            print("#################YOUR ACCOUNT CREATION IS DONE SUCESSFULLY###############")
        elif yy=="2":
            print(" ")
            print("YOUR ACCOUNT NUMBER IS :")
            val=random.randint(11111111,55555555)
            print(val)
            print(" ")
            print("YOUR CUSTOMER ID IS :")
            val1=random.randint(11111111,55555555)
            print(val1)
            amo=5000
            typ="SAVINGS"
            print(" ")
            print("SET PASSWORD FOR YOUR ACCOUNT!!!!!!!")
            pas=str(input())
            con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
            cur=con.cursor()
            sql = "insert into acco VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.d1,self.d2,self.d3,self.d4,self.d5,self.d6,val,val1,amo,typ,pas)
            cur.execute(sql)
            con.commit()
            print(" ")
            print("#######YOUR ACCOUNT CREATION IS DONE SUCESSFULLY---")
        else:
            print(" ")
            print("########ACCOUNT CREATION IS NOT DONE")
class creat(account):
    def logi(self):
        global acv
        global va1
        global kl
        global al
        global vq
        global rr
        global az
        global aoo
        global jjz
        print(" ")
        print("ENTER YOUR ACCOUNT NUMBER :")
        acv=str(input())
        con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
        cur=con.cursor()
        sql = "select accno from acco where accno='%s'" % (acv)
        cur.execute(sql)
        valu=cur.fetchone()
        if valu is None:
            print(" ")
            print("ACCOUNT NO YOU ENTERED IS WRONG PLEASE ENTER THE VALID NUMBER!!!!!!!!!!")
            vv=str(input())
            acv=vv
            sql = "select amo from acco where accno='%s'" % (vv)
            cur.execute(sql)
            valu1=cur.fetchone()
            print("")
            print("YOUR CURRENT BALANCE IS: ")
            print(valu1[0])
        else:
            sql = "select amo from acco where accno='%s'" % (acv)
            cur.execute(sql)
            valu1=cur.fetchone()
            print(" ")
            print("YOUR CURRENT BALANCE IS: ")
            print(valu1[0])
        sql = "select actyp from acco where accno='%s'" % (acv)
        cur.execute(sql)
        va1=cur.fetchone()
        print("")
        print("YOUR ACCCOUNT TYPE IS ")
        print(va1[0])
        print("")
        print("@@@ENTER YOUR CHOICE@@@@ ")
        print("1-update balance----")
        print("2-money transfer-----")
        print("3-money withdrawal----")
        print("4-Apply for the loan----")
        kl=str(input())
        if kl=="1":
            print("")
            print("ENTER THE AMOUNT TO UPDATE :")
            al=str(input())
            sql = "select amo from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vq=cur.fetchone()
            dd=vq[0]
            ff1=int(dd)+int(al)
            round(ff1)
            sql = "update acco set amo='%s' where accno='%s'" % (ff1,acv)
            cur.execute(sql)
            con.commit()
            print("")
            print("---YOUR AMOUNT IS UPDATED SUCESSFULLY--------------")
            print("")
            print("YOUR CURRENT BALANCE IS $ : ",ff1)
        elif kl=="2":
            print("")
            print("PLEASE ENTER YOUR ACCOUNT PASSWORD")
            iz=str(input())
            sql = "select password from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vq=cur.fetchone()
            oo=vq[0]
            if iz==oo:
                print("")
                print("PLEASE ENTER THE ACCOUNT NUMBER TO TRANSFER :")
                rr=str(input())
            else:
                print("")
                print("PLEASE ENTER THE CORRECT PASSWORD!!!!!!!!!!!!")
                ff=str(input())
                print("")
                print("PLEASE ENTER THE ACCOUNT NUMBER TO TRANSFER :")
                rr=str(input())
            sql = "select accno from acco where accno='%s'" % (rr)
            cur.execute(sql)
            vql=cur.fetchone()
            if vql is None:
                print("")
                print("PLEASE ENTER THE VALID ACCOUNT NUMBER!!!!!!")
                rr=str(input())
                print("")
                print("ENTER THE AMOUNT TO TRANSFER")
                az=str(input())
            else:
                print("")
                print("ENTER THE AMOUNT TO TRANSFER")
                az=str(input())
            print("")
            sql = "select amo from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vat=cur.fetchone()
            vat1=vat[0]
            llp=int(vat1)-int(az)
            sql = "select actyp from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vatll=cur.fetchone()
            vaty=vatll[0]
            if vaty=="CURRENT":
                aoo=1000
            else:
                aoo=5000
            print("")
            if llp<=aoo:
                print("!!!!!!YOU HAVE MINIMUM BALANCE AMOUNT TRANSFER IS NOT POSSIBLE!!!!!!!!")
            else:
                 sql = "update acco set amo='%s' where accno='%s'" % (llp,acv)
                 cur.execute(sql)
                 con.commit()
                 sql = "select amo from acco where accno='%s'" % (rr)
                 cur.execute(sql)
                 vatp=cur.fetchone()
                 bzz=vatp[0]
                 kkm=int(az)+int(bzz)
                 sql = "update acco set amo='%s' where accno='%s'" % (kkm,rr)
                 cur.execute(sql)
                 con.commit()
                 print("")
                 print("############MONEY TRANSFER IS DONE SUCESSFULLY-----")
        elif kl=="3":
            print("")
            print("PLEASE ENTER THE PASSWORD OF YOUR ACCOUNT :")
            iz=str(input())
            sql = "select password from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vq=cur.fetchone()
            oo=vq[0]
            if iz==oo:
                print("")
                print("PLEASE ENTER AMOUNT TO WITHDRAWAL :")
                rr=str(input())
            else:
                print("")
                print("PLEASE ENTER THE CORRECT PASSWORD!!!!!!!!!!!!")
                ff=str(input())
                print("PLEASE ENTER THE AMOUNT TO WITHDRAWAL------")
                rr=str(input())
            sql = "select amo from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vat=cur.fetchone()
            vat1=vat[0]
            llp=int(vat1)-int(rr)
            sql = "select actyp from acco where accno='%s'" % (acv)
            cur.execute(sql)
            vatll=cur.fetchone()
            vaty=vatll[0]
            if vaty=="CURRENT":
                aoo=1000
            else:
                aoo=5000
            print("")
            if llp<=aoo:
                print("YOU HAVE MINIMUM BALANCE AMOUNT WITHDRAWAL IS NOT POSSIBLE")
            else:
                 sql = "update acco set amo='%s' where accno='%s'" % (llp,acv)
                 cur.execute(sql)
                 con.commit()
                 print("AMOUNT WITHDRAWL IS DONE SUCESSFULLY-----")
        elif kl=="4":
           print("")
           print("PLEASE SUBMIT YOUR DOCUMENTS UNTILL IT IS VERIFIED BY MANAGER----- ")
           print(" ");
           print("YOUR LOAN ACCOUNT NUMBER----");
           loann=random.randint(11001111,99999995)
           print(loann)
           print("")
           print("ENTER THE LOAN AMOUNT: ")
           dx=str(input())
           sql = "select amo from acco where accno='%s'" % (acv)
           cur.execute(sql)
           vap=cur.fetchone()
           vap1=vap[0]
           loana=int(vap1)*2;
           print("Loan Amount for your account generated is : ",loana)
           con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
           cur=con.cursor()
           sql = "insert into loan VALUES('%s','%s','%s')" % (acv,loann,loana)
           cur.execute(sql)
           con.commit()
class fix(account):
    def depso(self):
        global jjz
        global qpp
        global zz
        global x7
        print("")
        print("ARE YOU INTEREST IN FIXED DEPOSIT yes/no");
        vza=str(input())
        print("")
        print("ENTER THE CUSTOMER ID")
        zz=str(input())
        if vza=="yes":
             print("")
             con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
             cur=con.cursor()   
             sql = "select cusid from acco where cusid='%s'" % (zz)
             cur.execute(sql)
             vq=cur.fetchone()
             if vq is None:
                 print(" ")
                 print("CUSTOMER ID YOU ENTERED IS WRONG PLEASE ENTER THE VALID ID!!!!!!!!!!1")
                 vv=str(input())
                 zz=vv
                 print("")
                 print("ENTER THE INITIAL AMOUNT TO DEPOSIT :")
                 jjz=str(input())
             else:
                 print("")
                 print("ENTER THE INITIAL AMOUNT TO DEPOSIT :")
                 jjz=str(input())
             con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
             cur=con.cursor()
             sql = "select amo from acco where cusid='%s'" % (zz)
             cur.execute(sql)
             gb=cur.fetchone()
             nb=gb[0]
             print("")
             print("YOUR BALANCE IN SAVINGS ACCOUNT IS : ",nb);
             print(" ")
             print("YOUR FIXED DEPOSIT ACCOUNT  NUMBER IS : ")
             vc=random.randint(11111111,55555555)
             print(vc)
             aqv=int(jjz)+int(nb)
             print(" ")
             print("YOUR BALANCE : FIXED AMOUNT + SAVINGS:")
             print(aqv)
             print(" ")
             print("INTEREST CALCULATION IS ABOUT 6% PER ANNUM OF YOUR SAVINGS ACCOUNT--")
             print(" ")
             qw=(6/100)*aqv
             pz=aqv-qw
             print(" ")
             print("YOUR INTEREST AMOUNT PER ANNUM IS :" , qw)
             con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
             cur=con.cursor()
             sql = "insert into fixe values('%s','%s','%s')" %(zz,vc,aqv)
             cur.execute(sql)
             con.commit()
        else:
            print("##############THANK YOU#####################")
        print(" ")
        print("WANT TO ALTER DATABASE ???? yes/no")
        xc=str(input())
        if xc=="yes":
            print("1-Address--")
            print("2-City--")
            print("3-State--")
            print("4-Pincode--")
            qpp=str(input())
            if qpp=="1":
                print("")
                print("ENTER YOUR NEW ADDRESS :")
                a1=str(input())
                con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
                cur=con.cursor()
                sql = "update acco set address='%s' where cusid='%s'" % (a1,zz)
                cur.execute(sql)
                con.commit()
                print(" ")
                print("YOUR MODIFICATIONS ARE DONE SUCESSFULLY-----")
            elif qpp=="2":
                print("")
                print("ENTER YOUR NEW CITY :")
                a1=str(input())
                con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
                cur=con.cursor()
                sql = "update acco set city='%s' where cusid='%s'" % (a1,zz)
                cur.execute(sql)
                con.commit()
                print(" ")
                print("YOUR MODIFICATIONS ARE DONE SUCESSFULLY-----")
            elif qpp=="3":
                print("")
                print("ENTER YOUR NEW STATE :")
                a1=str(input())
                con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
                cur=con.cursor()
                sql = "update acco set state='%s' where cusid='%s'" % (a1,zz)
                cur.execute(sql)
                con.commit()
                print(" ")
                print("YOUR MODIFICATIONS ARE DONE SUCESSFULLY-----")
            elif qpp=="4":
                print("")
                print("ENTER YOUR NEW PINCODE :")
                a1=str(input())
                con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
                cur=con.cursor()
                sql = "update acco set pincode='%s' where cusid='%s'" % (a1,zz)
                cur.execute(sql)
                con.commit()
                print(" ")
                print("YOUR MODIFICATIONS ARE DONE SUCESSFULLY-----")
        else:
           print(" ")
           print("######THANK YOU---")
           print(" ")
        print(" DO YOU WANT TO SEE CUSTOMER DETAILS yes/no")
        mxx=str(input())
        if mxx=="yes":
            print("" )
            print("------------------------------------------------------")
            print("---------------CUSTOMER DETAILS------------------------")
            print("-------------------------------------------------------")
            con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
            cur=con.cursor()
            sql = "select fname from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au2=cur.fetchone()
            x1=au2[0]
            print("CUSTOMER FIRST NAME : ",x1)
            sql = "select lname from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au3=cur.fetchone()
            x2=au3[0]
            print("CUSTOMER LAST NAME : ",x2)
            sql = "select address from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au4=cur.fetchone()
            x3=au4[0]
            print("CUSTOMER ADDRESS  : ",x3)
            sql = "select city from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au5=cur.fetchone()
            x13=au5[0]
            print("CUSTOMER CITY: ",x13)
            sql = "select pincode from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au6=cur.fetchone()
            x6=au6[0]
            print("PINCODE :",x6)
            sql = "select accno from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au7=cur.fetchone()
            x7=au7[0]
            print("ACCOUNT NUMBER :",x7)
            sql = "select cusid from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au8=cur.fetchone()
            x8=au8[0]
            print("CUSTOMER ID NUMBER :",x8)
            sql = "select actyp from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au9=cur.fetchone()
            x9=au9[0]
            print("CUSTOMER ACCOUNT TYPE IS: ",x9)
            sql = "select amo from acco where cusid='%s'" % (zz)
            cur.execute(sql)
            au10=cur.fetchone()
            x10=au10[0]
            print("AMOUNT IN YOUR ACCOUNT  IS: ",x10)
class demo(account,creat,fix):
    while(1):
        print("")
        print("----------------####WELCOME TO BANK OF  BARODA######----------------------")
        print(" ")
        print("-----********INDIA'S INTERNATIONAL BANK*************-----------")
        print(" ")
        print("**********ALREADY HAVE ACCOUNT yes/no")
        d=str(input())
        if d=="yes":
            print(" ")
            print("###########LOGIN WITH YOUR ACCOUNT")
            v=creat()
            v.logi()
            gg=fix()
            gg.depso()
            print(" ")
        else:
            print(" ")
            print("!!!!!!!!!ACCOUNT CREATION----------------")
            n1=account()
            n1.acc()
        print("")
        print("DO YOU WANT TO CLOSE YOUR ACCOUNT!!!!! yes/no")
        fg=str(input())
        if fg=="yes":
            print(" ")
            print("ENTER THE ACOUNT NUMBER")
            az=str(input())
            print("")
            print("ENTER THR PASSWORD !!!!!!!!!!")
            azz=str(input())
            print("YOUR ACCOUNT IS DELETED SHORTLY-------")
        else:
            print("")
            print("##############THANK YOU VISIT AGAIN###############################")

        
