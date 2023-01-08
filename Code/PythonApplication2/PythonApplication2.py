from tkinter import *
from pymysql import *
from PIL import ImageTk, Image

db=connect(host="localhost",user="root",password="147852",database="trade")
cursor=db.cursor()

#错误提示
def eeer(x1,x2):
    tt=('校园二手交易系统--{}').format(x1)
    fail=Toplevel()
    fail.title(tt)
    fail.resizable(0,0)
    canvas = Canvas(fail,width=400,height=150,bd=0, highlightthickness=0)
    canvas.create_image(50,50, image=photo3)
    canvas.grid(row=0,column=0)

    width=400
    heigh=150
    screenwidth = fail.winfo_screenwidth()
    screenheight = fail.winfo_screenheight()
    fail.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
            
    ll1=Label(fail,text=x2)
    Bb1=Button(fail,text="   确定   ",command=fail.destroy)
    canvas.create_window(200,50,window=ll1)
    canvas.create_window(200,110,window=Bb1)
    return
#成功提示
def succ(x1,x2):
    tt=('校园二手交易系统--{}').format(x1)
    success=Toplevel()
    success.resizable(0,0)
    success.title(tt)
    canvas = Canvas(success,width=400,height=150,bd=0, highlightthickness=0)
    canvas.create_image(50,50, image=photo4)
    canvas.grid(row=0,column=0)
    width=400
    heigh=150
    screenwidth = success.winfo_screenwidth()
    screenheight = success.winfo_screenheight()
    success.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    ll3=Label(success,text=x2)
    Bb3=Button(success,text="   确定   ",command=success.destroy)
    canvas.create_window(200,50,window=ll3)
    canvas.create_window(200,110,window=Bb3)
    return

#用户登录界面
def new():
    basic1=Toplevel()
    basic1.resizable(0,0)
    #居中弹窗
    screenwidth = basic1.winfo_screenwidth()
    screenheight = basic1.winfo_screenheight()
    width=299
    heigh=300
    basic1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

    #背景
    canvas = Canvas(basic1,width=299,height=300,bd=0, highlightthickness=0)
    canvas.create_image(150,53, image=photo1)

    canvas.grid(row=0,column=0)
  
    LL1=Label(basic1,text='账号:')
    LL2=Label(basic1,text='密码:')

    v1=StringVar()
    v2=StringVar()

    e1=Entry(basic1,textvariable=v1)
    e2=Entry(basic1,textvariable=v2,show='*')

    canvas.create_window(90,150,window=LL1)
    canvas.create_window(90,180,window=LL2)
    canvas.create_window(170,150,width=120,window=e1)
    canvas.create_window(170,180,width=120,window=e2)

    def login():
        
        #输入框获取用户名密码
        uid=v1.get()
        password=v2.get()

        sql='select uid,uname,password from user where uid="{}"'.format(uid)
        cursor.execute(sql)
        
        if not cursor.rowcount:
            a='登录'
            b='账号不存在！'
            eeer(a,b)
            return
        qwert=cursor.fetchone()
        if qwert[2]!=password:
            a='登录'
            b='密码错误！'
            eeer(a,b)
            return
        list(qwert)
        basic1.destroy()
        afterLog(qwert[1])
    def xiuxiu():
        basic2=Toplevel()
        basic2.resizable(0,0)
        #居中弹窗
        screenwidth = basic2.winfo_screenwidth()
        screenheight = basic2.winfo_screenheight()
        width=299
        heigh=250
        basic2.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

            #背景
        canvas2 = Canvas(basic2,width=299,height=250,bd=0, highlightthickness=0)
        canvas2.create_image(150,32, image=photo19)
        canvas2.grid(row=0,column=0)
  
        LLL1=Label(basic2,text='账号:')
        LLL2=Label(basic2,text='原密码:')
        LLL3=Label(basic2,text='新密码:')

        vv1=StringVar()
        vv2=StringVar()
        vv3=StringVar()

        ee1=Entry(basic2,textvariable=vv1)
        ee2=Entry(basic2,textvariable=vv2,show='*')
        ee3=Entry(basic2,textvariable=vv3,show='*')

        canvas2.create_window(90,80,window=LLL1)
        canvas2.create_window(85,110,window=LLL2)
        canvas2.create_window(85,140,window=LLL3)

        canvas2.create_window(170,80,width=120,window=ee1)
        canvas2.create_window(170,110,width=120,window=ee2)
        canvas2.create_window(170,140,width=120,window=ee3)


        def ooo1():
            uuid=vv1.get()
            ppassword=vv2.get()
            newpassword=vv3.get()
            sql='select uid,password from user where uid="{}"'.format(uuid)
            cursor.execute(sql)
            if not cursor.rowcount:
                a='修改密码'
                b='账号不存在！'
                eeer(a,b)
                return
            if cursor.fetchone()[1]!=ppassword:
                a='修改密码'
                b='原密码错误！'
                eeer(a,b)
                return
            sql='update user set password="{}" where uid="{}"'.format(newpassword,uuid)
            cursor.execute(sql)
            db.commit()
            hugy='修改密码'
            hjjk='修改密码成功！'
            succ(hugy,hjjk)
            basic2.destroy()
        BB3=Button(basic2,text='立即修改',width=10,command=ooo1)
        canvas2.create_window(150,200,window=BB3)
        return




    BB1=Button(basic1,text='立即登录',width=10,command=login)
    BB2=Button(basic1,text='修改密码',width=10,command=xiuxiu)
    canvas.create_window(150,230,window=BB1)
    canvas.create_window(150,270,window=BB2)
    return


def afterLog(x):
    #检测是否是管理员
    sql="select Admin from user where uname='{}'".format(x)
    cursor.execute(sql)
    content=cursor.fetchone()
    a=int(content[0])

    #管理员界面
    if a==1:
        new=Toplevel()
        new.title("校园二手交易系统--%s" % x)
        new.geometry('620x400')

        w=300
        h=150
        new.resizable(0,0)
        screenwidth = new.winfo_screenwidth()
        screenheight = new.winfo_screenheight()
        new.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2, (screenheight-h)/2))

        canvas = Canvas(new,width=w,height=h,bd=0, highlightthickness=0)
        canvas.create_image(50,70, image=photo15)
        canvas.grid(row=0,column=0)



        #修改个人信息，查看商品，发布商品
        #用户管理
        def users():
            user=Toplevel()
            user.title('校园二手交易系统--用户管理')
            u1=LabelFrame(user,text='用户管理',font=('宋体',12))
            u1.grid(row=0,column=0,padx=10,pady=10)

            user.update()
            w=user.winfo_width()
            h=user.winfo_height()
            user.resizable(0,0)
            screenwidth = user.winfo_screenwidth()
            screenheight = user.winfo_screenheight()
            user.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-450, (screenheight-h)/2-225))

            u2=Frame(u1)
            u2.grid(row=0,column=0,padx=10,pady=10)
            Label(u2,anchor='w',text='账号                                                             用户名                                                           密码                                                             管理权限',width=135).grid(row=0,column=0,sticky='W')
            LB = Listbox(u2,setgrid=True,font=('YaHei Consolas Hybrid',12))
            LB.grid(row=2,column=0)
            LB.config(height=20,width=120)


            scr1=Scrollbar(u2)
            LB.config(yscrollcommand=scr1.set)
            scr1.config(command=LB.yview)
            scr1.grid(row=2,column=1,sticky='ns')



            sql='select * from user where uname!="{}"'.format(x)
            cursor.execute(sql)

            temp4=cursor.rowcount
            while temp4>0:
                    t=cursor.fetchone()
                    t=list(t)
                    if t[3]=='1':
                        t[3]='管理员'
                    elif t[3]=='0':
                        t[3]='普通用户'
                    jk=[]
                    for item in t:
                        cha=str(item)
                        leng=len(cha)
                        for item1 in cha:
                            if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                                leng+=1
                        while(leng<30):
                            cha=cha+' '
                            leng+=1
                        jk.append(cha)
                    jk[3]=str(jk[3])

                    for item2 in [jk[0]+jk[1]+jk[2]+jk[3]]:
                        LB.insert(END,item2)
                    temp4=temp4-1

            def back1():
                
                b1=list(LB.get(ACTIVE))
                mmm=0
                #补齐缺少的空格
                for each in b1:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b1.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1
                c1=[0,1,2]
                temp6=3
                k=0
                k1=0
                c1[0]=b1[0]
                c1[1]=b1[30]
                c1[2]=b1[60]
                while temp6:
                    fill1=29
                    k1+=1
                    while fill1:
                        if b1[k1]!=' ':
                            c1[k]=c1[k]+b1[k1]
                            k1+=1
                            fill1-=1

                        else:
                            k1+=1
                            fill1-=1
                    k+=1
                    temp6-=1
                return c1
            #封账号
            def close():
                ff=back1()
                LB.delete(ACTIVE)
                sql='delete from wishlist where uname="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()
                sql='delete from wishlist where seller="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()
                    
                sql='delete from orders where buyer="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()
                sql='delete from orders where seller="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()

                sql='delete from goods where seller="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()
                sql='delete from user where uid="{}"'.format(ff[0])
                cursor.execute(sql)
                db.commit()
                
                return
            #设置管理员
            def upup():
                new5=Toplevel()
                new5.title('校园二手交易系统--用户管理')

                w=291
                h=140
                new5.resizable(0,0)
                screenwidth = new5.winfo_screenwidth()
                screenheight = new5.winfo_screenheight()
                new5.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2, (screenheight-h)/2))
                canvas = Canvas(new5,width=w,height=h,bd=0, highlightthickness=0)
                canvas.create_image(40,60, image=photo10)
                canvas.grid(row=0,column=0)

                ll1=Label(new5,text='请输入改动秘钥:')
                c1=StringVar()
                pro1=Entry(new5,textvariable=c1,width=15,show='*')
                canvas.create_window(130,55,window=ll1)
                canvas.create_window(230,55,window=pro1)
                def gai():
                    g=c1.get()
                    #此处可设置改动秘钥
                    if g=='857857':
                        u=back1()
                        sql='update user set admin=1 where uname="{}"'.format(u[1])
                        cursor.execute(sql)
                        db.commit()
                        new5.destroy()
                        user.destroy()
                        aa='用户管理'
                        bb='设置成功！'
                        succ(aa,bb)
                        return
                    else:
                        aa='用户管理'
                        bb='改动秘钥错误！'
                        eeer(aa,bb)
                        return
                bbb=Button(new5,text="提交",command=gai)
                canvas.create_window(146,100,window=bbb)
            #降级管理员
            def down():
                new5=Toplevel()
                new5.title('校园二手交易系统--用户管理')
                w=291
                h=140
                new5.resizable(0,0)
                screenwidth = new5.winfo_screenwidth()
                screenheight = new5.winfo_screenheight()
                new5.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2, (screenheight-h)/2))
                canvas = Canvas(new5,width=w,height=h,bd=0, highlightthickness=0)
                canvas.create_image(40,60, image=photo10)
                canvas.grid(row=0,column=0)
                ll1=Label(new5,text='请输入改动秘钥:')
                c1=StringVar()
                pro1=Entry(new5,textvariable=c1,width=15,show='*')
                canvas.create_window(130,55,window=ll1)
                canvas.create_window(230,55,window=pro1)
                def gai():
                    g=c1.get()
                    #此处可设置改动秘钥
                    if g=='857857':
                        u=back1()
                        sql='update user set admin=0 where uname="{}"'.format(u[1])
                        cursor.execute(sql)
                        db.commit()
                        new5.destroy()
                        user.destroy()

                        aa='用户管理'
                        bb='降级成功！'
                        succ(aa,bb)
                        return
                    else:
                        aa='用户管理'
                        bb='改动秘钥错误！'
                        eeer(aa,bb)
                        return
                bbb=Button(new5,text="提交",command=gai)
                canvas.create_window(146,100,window=bbb)

            Button(user,text="封禁用户",command=close,width=15).grid(row=2,column=0)
            Button(user,text="设置为管理员",command=upup,width=15).grid(row=3,column=0)
            Button(user,text="降级",width=15,command=down).grid(row=4,column=0)
        #商品管理
        def commodities():
            goods=Toplevel()
            goods.title('校园二手交易系统--商品管理')

            goods.update()
            w=goods.winfo_width()
            h=goods.winfo_height()
            goods.resizable(0,0)
            screenwidth = goods.winfo_screenwidth()
            screenheight = goods.winfo_screenheight()
            goods.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-530, (screenheight-h)/2-225))

            g1=LabelFrame(goods,text='商品管理',font=('宋体',12))
            g1.grid(row=0,column=0,padx=10,pady=10)

            g2=Frame(g1)
            g2.grid(row=0,column=0,padx=10,pady=10)
            Label(g2,anchor='w',text='卖家                                                              商品编号                                                        商品名称                                                      单价                                                             库存',width=168).grid(row=0,column=0,sticky='W')
            LB1 = Listbox(g2,setgrid=True,font=('YaHei Consolas Hybrid',12))
            LB1.grid(row=2,column=0)
            LB1.config(height=20,width=150)


            scr2=Scrollbar(g2)
            LB1.config(yscrollcommand=scr2.set)
            scr2.config(command=LB1.yview)
            scr2.grid(row=2,column=1,sticky='ns')

            sql='select * from goods'
            cursor.execute(sql)

            temp6=cursor.rowcount

           
            while temp6>0:

                    t=cursor.fetchone()
                    t=list(t)
                    jk=[]
  
                    for item in t:
                        cha=str(item)
                        leng=len(cha)
                        for item1 in cha:
                            if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                                leng+=1
                        while(leng<30):
                            cha=cha+' '
                            leng+=1
                        jk.append(cha)
                    for item2 in [jk[0]+jk[1]+jk[2]+jk[3]+jk[4]]:
                            LB1.insert(END,item2)
                    temp6=temp6-1

            def back2():
                
                b1=list(LB1.get(ACTIVE))
                mmm=0
                for each in b1:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b1.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1
                c1=[0,1,2,3,4]
                temp8=5
                k=0
                k1=0
                c1[0]=b1[0]
                c1[1]=b1[30]
                c1[2]=b1[60]
                c1[3]=b1[90]
                c1[4]=b1[120]
                while temp8:
                    fill1=29
                    k1+=1
                    while fill1:
                        if b1[k1]!=' ':
                            c1[k]=c1[k]+b1[k1]
                            k1+=1
                            fill1-=1
                        else:
                            k1+=1
                            fill1-=1
                    k+=1
                    temp8-=1
                return c1
            def close1():
                ff=back2()
                LB1.delete(ACTIVE)
                sql='delete from wishlist where gno="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()

                sql='delete from orders where gno="{}"'.format(ff[1])
                cursor.execute(sql)
                db.commit()

                sql='SET FOREIGN_KEY_CHECKS = 0'
                cursor.execute(sql)
                sql='delete from goods where gno="{}"'.format(ff[1])
                cursor.execute(sql)
                sql='SET FOREIGN_KEY_CHECKS = 1'
                cursor.execute(sql)
                db.commit()

            Button(goods,text="下架商品",command=close1).grid(row=2,column=0)

        BB1=Button(new,text="用户管理",command=users)
        BB2=Button(new,text="商品管理",command=commodities)
        canvas.create_window(130,70,window=BB1)
        canvas.create_window(210,70,window=BB2)

    #普通用户界面
    else:
        new1=Toplevel()
        new1.title("校园二手交易系统--%s" % x)
        new1.resizable(0,0)
        width=650
        heigh=365
        screenwidth = new1.winfo_screenwidth()
        screenheight = new1.winfo_screenheight()
        new1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
        
        canvas = Canvas(new1,width=650,height=365,bd=0, highlightthickness=0)
        canvas.create_image(325,182,image=photo5)
        canvas.grid(row=0,column=0)


        #修改个人信息，查看商品，发布商品
        #修改个人信息
        #def xiuxiu():

        #发布商品
        def publish():
            new2=Toplevel()
            new2.title("校园二手交易系统--发布商品")
            
            width=670
            heigh=444
            new2.resizable(0,0)
            screenwidth = new2.winfo_screenwidth()
            screenheight = new2.winfo_screenheight()
            new2.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

            canvas = Canvas(new2,width=670,height=444,bd=0, highlightthickness=0)

            canvas.create_image(335,59, image=photo6)
            canvas.create_image(89,222, image=photo7)
            canvas.create_image(581,222, image=photo8)
            canvas.create_image(335,385,image=photo9)

            canvas.grid(row=0,column=0)

            ll1=Label(new2,text='商品编号:')
            ll2=Label(new2,text='商品名称:')
            ll3=Label(new2,text='商品单价:')
            ll4=Label(new2,text='商品个数:')
            c1=StringVar()
            c2=StringVar()
            c3=StringVar()
            c4=StringVar()
            p1=Entry(new2,textvariable=c1)
            p2=Entry(new2,textvariable=c2)
            p3=Entry(new2,textvariable=c3)
            p4=Entry(new2,textvariable=c4)

            canvas.create_window(250,147,window=ll1)
            canvas.create_window(250,187,window=ll2)
            canvas.create_window(250,227,window=ll3)
            canvas.create_window(250,267,window=ll4)

            canvas.create_window(360,147,window=p1)
            canvas.create_window(360,187,window=p2)
            canvas.create_window(360,227,window=p3)
            canvas.create_window(360,267,window=p4)

            def pub():
                gno=c1.get()
                gname=c2.get()
                #检验单价和个数的数值类型
                try:
                    price=float(c3.get())
                    num=int(c4.get())
                    #查询数据库中商品编号是否已存在
                    sql='select gno from goods where gno="{}"'.format(gno)
                    cursor.execute(sql)
                    if cursor.rowcount:
                        a='发布商品'
                        b='商品编号已存在！'
                        eeer(a,b)
                        return
                    sql='insert into goods values("{}","{}","{}","{}","{}")'.format(x,gno,gname,price,num)
                    cursor.execute(sql)
                    db.commit()
                    a='发布商品'
                    b='发布成功！'
                    succ(a,b)
                    return
                except:
                    a='发布商品'
                    b='单价/个数必须为数字！'
                    eeer(a,b)
                    return
            
            bbb=Button(new2,text="立即发布",comman=pub)
            canvas.create_window(335,307,window=bbb)
            return
        #升级为管理员
        def promote():
            pro=Toplevel()

            w=291
            h=140
            pro.resizable(0,0)
            screenwidth = pro.winfo_screenwidth()
            screenheight = pro.winfo_screenheight()
            pro.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2, (screenheight-h)/2))
            canvas = Canvas(pro,width=w,height=h,bd=0, highlightthickness=0)

            canvas.create_image(40,60, image=photo10)
            canvas.grid(row=0,column=0)



            ll1=Label(pro,text='请输入秘钥:')
            p1=StringVar()
            pro1=Entry(pro,textvariable=p1,width=15,show='*')

            canvas.create_window(130,55,window=ll1)
            canvas.create_window(230,55,window=pro1)

            def verify():
                p=p1.get()
                #此处可设置秘钥
                if p=='147852':
                    sql='update user set admin=1 where uname="{}"'.format(x)
                    cursor.execute(sql)
                    db.commit()


                    pro.destroy()
                    new1.destroy()
                    a='升级管理员'
                    b='升级成功！请重新登录'
                    succ(a,b)
                    return
                else:
                    a='升级管理员'
                    b='秘钥无效！'
                    eeer(a,b)
                    return
            bbb=Button(pro,text="立即升级!",command=verify)
            canvas.create_window(146,100,window=bbb)
        #逛商城
        def hang():
            new3=Toplevel()
            new3.title("校园二手交易系统--商城")

            new3.update()
            w=new3.winfo_width()
            h=new3.winfo_height()

            new3.resizable(0,0)
            screenwidth = new3.winfo_screenwidth()
            screenheight = new3.winfo_screenheight()
            new3.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-419, (screenheight-h)/2-250))

            canvas = Canvas(new3,width=1058,height=145,bd=0, highlightthickness=0)
            canvas.create_image(529,72, image=photo12)
            canvas.grid(row=0,column=0)
            


          
            ss1=LabelFrame(new3,text='商城')
            ss1.grid(row=1,column=0,padx=10,pady=10)
            ss2=Frame(ss1)
            ss2.grid(row=0,column=0,padx=10,pady=10)
            Label(ss2,anchor='w',text='卖家                                                              商品编号                                                       商品名称                                                       单价',width=120).grid(row=0,column=0,sticky='W')

            theLB = Listbox(ss2,setgrid=True,font=('YaHei Consolas Hybrid',12))
            theLB.grid(row=2,column=0)
            theLB.config(height=20,width=110)

            scr=Scrollbar(ss2)
            theLB.config(yscrollcommand=scr.set)
            scr.config(command=theLB.yview)
            scr.grid(row=2,column=1,sticky='ns')

            sql='select * from goods where num>0'
            cursor.execute(sql)
            #插入表的数据
            temp2=cursor.rowcount
            while temp2>0:
                t=cursor.fetchone()
                t=list(t)
                jk=[]
  
                for item in t:
                    cha=str(item)
                    leng=len(cha)
                    for item1 in cha:
                        if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                            leng+=1
                    while(leng<30):
                        cha=cha+' '
                        leng+=1
                    jk.append(cha)
                for item2 in [jk[0]+jk[1]+jk[2]+jk[3]]:
                        theLB.insert(END,item2)
                temp2=temp2-1
            #返回选中的数据
            def back():
                b=list(theLB.get(ACTIVE))
                #不赋初值之后会提示out of range
                mmm=0
                for each in b:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1
                c=[0,1,2,3]
                #表有5个项
                temp1=4
                k=0#指定c元素的位置
                k1=0#记录b元素的位置
                #每一项的第一个字
                c[0]=b[0]
                c[1]=b[30]
                c[2]=b[60]
                c[3]=b[90]
                while temp1:
                    fill1=29
                    #去空格
                    k1+=1
                    while fill1:
                        if b[k1]!=' ':
                            c[k]=c[k]+b[k1]
                            k1+=1
                            fill1-=1
                        else:
                            k1+=1
                            fill1-=1
                    k+=1
                    temp1-=1
                sql='select * from goods where gno="{}"'.format(c[1])
                cursor.execute(sql)
                eee=cursor.fetchone()
                c.append(eee[4])
                return c     
            #下单功能#库存为0即刻删除#买了以后从愿望单删除
            def BuyBuyBuy():
                a=back()
                #a[0]卖家，a[1]商品编号，a[2]商品名称，a[3]单价，a[4]库存
                kk=a[4]
                kkinfo='当前库存:   {}'.format(kk)
                sql='select * from orders where gno="{}" and buyer="{}"'.format(a[1],x)
                cursor.execute(sql)
                if cursor.rowcount:

                    a='商城'
                    b='您已购买过该商品,请先完成之前的订单！'
                    eeer(a,b)
                    return
                if a[0]==x:
                    a='商城'
                    b='您不能购买自己发布的商品！'
                    eeer(a,b)
                    return

                buy1=Toplevel()
                buy1.title('校园二手交易系统--商城')
                buy1.resizable(0,0)
                canvas = Canvas(buy1,width=400,height=150,bd=0, highlightthickness=0)
                canvas.create_image(50,50, image=photo11)
                canvas.grid(row=0,column=0)
                width=400
                heigh=150
                screenwidth = buy1.winfo_screenwidth()
                screenheight = buy1.winfo_screenheight()
                buy1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
                ll0=Label(buy1,text=kkinfo)
                ll1=Label(buy1,text='购买数量:')
                ll2=Label(buy1,text='收货地址:')

                canvas.create_window(130,15,window=ll0)
                canvas.create_window(120,50,window=ll1)
                canvas.create_window(120,85,window=ll2)

                q1=StringVar()
                q2=StringVar()
                w1=Entry(buy1,textvariable=q1)
                w2=Entry(buy1,textvariable=q2)


                canvas.create_window(230,50,window=w1)
                canvas.create_window(230,85,window=w2)

                def sub():
                    try:
                        add=q2.get()
                        qua=q1.get()
                        a=back()
                        a.append(add)
                        a.append(qua)
                        
                        cost=float(a[3])*int(a[6])
                    except:
                        a='商城'
                        b='输入的数量必须为数字！'
                        eeer(a,b)
                        return
                    #a[4]库存，a[6]购买数量
                    kkk=int(a[4])
                    a[6]=int(a[6])
                   

                    #检查库存
                    if (kkk<a[6]):
                        aa='商城'
                        bb='库存不足！请检查购买数量！'
                        eeer(aa,bb)
                        return
                    else:
                        a.append(cost)
                        a.append(x)
                        sql='insert into orders values("{}","{}","{}","{}","{}","{}","{}")'.format(x,a[0],a[1],a[2],add,qua,cost)
                        cursor.execute(sql)
                        db.commit()
                        a[6]=kkk-a[6]
                        ddd=int(a[6])

                        sql='update goods set num="{}" where gno="{}"'.format(a[6],a[1])
                        cursor.execute(sql)
                        db.commit()
                        

                        buy1.destroy()

                        aaaa='商城'
                        bbbb='购买成功！'
                        succ(aaaa,bbbb)
                        #如果一次都买完了则从列表里删除该商品
                        if ddd==0:
                            theLB.delete(ACTIVE)
                        #如果在愿望单里，买完后从愿望单里删除
                        sql='select * from wishlist where uname="{}" and gno="{}"'.format(x,a[1])
                        cursor.execute(sql)
                        ttt=cursor.rowcount
                        if ttt==1:
                            sql='delete from wishlist where uname="{}" and gno="{}"'.format(x,a[1])
                            cursor.execute(sql)
                            db.commit()
                        return

                Bb3=Button(buy1,text="立即下单",command=sub)
                canvas.create_window(200,130,window=Bb3)          
            #添加到心愿单功能
            def add():
                a=back()
                sql='select * from orders where gno="{}" and buyer="{}"'.format(a[1],x)
                cursor.execute(sql)
                if cursor.rowcount:
                    a='商城'
                    b='添加失败因为您已买到该商品喽~'
                    eeer(a,b)
                    return
                sql='select * from wishlist where gno="{}" and uname="{}"'.format(a[1],x)
                cursor.execute(sql)
                if cursor.rowcount:
                    a='商城'
                    b='您已添加过该商品,请勿重复添加！'
                    eeer(a,b)
                    return

                sql='select * from goods where gno="{}" and seller="{}"'.format(a[1],x)
                cursor.execute(sql)
                if cursor.rowcount:
                    a='商城'
                    b='您不能添加自己发布的商品！'
                    eeer(a,b)
                    return

                sql='insert into wishlist values("{}","{}","{}","{}","{}")'.format(x,a[0],a[1],a[2],float(a[3]))
                cursor.execute(sql)
                db.commit()
                a='商城'
                b='添加成功！'
                succ(a,b)
                return
            #搜索商品功能
            def ser():
                sou=Toplevel()
                sou.resizable(0,0)
                sou.title('校园二手交易系统--搜索商品')
                canvas = Canvas(sou,width=400,height=150,bd=0, highlightthickness=0)
                canvas.create_image(50,50, image=photo18)
                canvas.grid(row=0,column=0)
                width=400
                heigh=150
                screenwidth = sou.winfo_screenwidth()
                screenheight = sou.winfo_screenheight()
                sou.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

                ll3=Label(sou,text='商品名称:')
                q2=StringVar()
                w1=Entry(sou,textvariable=q2)

                def chulai():
                    sou.destroy()
                    chu=Toplevel()
                    

                    chu.update()
                    w=chu.winfo_width()
                    h=chu.winfo_height()

                    chu.resizable(0,0)
                    screenwidth = chu.winfo_screenwidth()
                    screenheight = chu.winfo_screenheight()
                    chu.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-455, (screenheight-h)/2-250))



                    ss1=LabelFrame(chu,text='商城')
                    ss1.grid(row=1,column=0,padx=10,pady=10)
                    ss2=Frame(ss1)
                    ss2.grid(row=0,column=0,padx=10,pady=10)
                    Label(ss2,anchor='w',text='卖家                                                              商品编号                                                       商品名称                                                       单价',width=120).grid(row=0,column=0,sticky='W')

                    theLB1= Listbox(ss2,setgrid=True,font=('YaHei Consolas Hybrid',12))
                    theLB1.grid(row=1,column=0)
                    theLB1.config(height=20,width=120)

                    sql='select * from goods where gname="{}" and seller!="{}" and num>0'.format(q2.get(),x)
                    cursor.execute(sql)
                    temp2=cursor.rowcount
                    while temp2>0:
                        t=cursor.fetchone()
                        t=list(t)
                        jk=[]
  
                        for item in t:
                            cha=str(item)
                            leng=len(cha)
                            for item1 in cha:
                                if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                                    leng+=1
                            while(leng<30):
                                cha=cha+' '
                                leng+=1
                            jk.append(cha)
                        for item2 in [jk[0]+jk[1]+jk[2]+jk[3]]:
                                theLB1.insert(END,item2)
                        temp2=temp2-1

                        def back1():
                            b=list(theLB1.get(ACTIVE))
                            #不赋初值之后会提示out of range
                            mmm=0
                            for each in b:
                                if u'\u4e00' <= each <= u'\u9fa5':
                                    b.insert(mmm+1,' ')
                                    mmm+=1
                                else:
                                    mmm+=1
                            c=[0,1,2,3]
                            #表有5个项
                            temp1=4
                            k=0#指定c元素的位置
                            k1=0#记录b元素的位置
                            #每一项的第一个字
                            c[0]=b[0]
                            c[1]=b[30]
                            c[2]=b[60]
                            c[3]=b[90]
                            while temp1:
                                fill1=29
                                #去空格
                                k1+=1
                                while fill1:
                                    if b[k1]!=' ':
                                        c[k]=c[k]+b[k1]
                                        k1+=1
                                        fill1-=1
                                    else:
                                        k1+=1
                                        fill1-=1
                                k+=1
                                temp1-=1
                            sql='select * from goods where gno="{}"'.format(c[1])
                            cursor.execute(sql)
                            eee=cursor.fetchone()
                            c.append(eee[4])
                            return c     
                        #下单功能#库存为0即刻删除#买了以后从愿望单删除
                        def BuyBuyBuy1():
                            a=back1()
                            #a[0]卖家，a[1]商品编号，a[2]商品名称，a[3]单价，a[4]库存
                            kk=a[4]
                            kkinfo='当前库存:   {}'.format(kk)
                            sql='select * from orders where gno="{}" and buyer="{}"'.format(a[1],x)
                            cursor.execute(sql)
                            if cursor.rowcount:
                                a='商城'
                                b='您已购买过该商品,请先完成之前的订单！'
                                eeer(a,b)
                                return
                            if a[0]==x:
                                a='商城'
                                b='您不能购买自己发布的商品！'
                                eeer(a,b)
                                return

                            buy1=Toplevel()
                            buy1.title('校园二手交易系统--商城')
                            buy1.resizable(0,0)
                            canvas = Canvas(buy1,width=400,height=150,bd=0, highlightthickness=0)
                            canvas.create_image(50,50, image=photo11)
                            canvas.grid(row=0,column=0)
                            width=400
                            heigh=150
                            screenwidth = buy1.winfo_screenwidth()
                            screenheight = buy1.winfo_screenheight()
                            buy1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
                            ll0=Label(buy1,text=kkinfo)
                            ll1=Label(buy1,text='购买数量:')
                            ll2=Label(buy1,text='收货地址:')

                            canvas.create_window(130,15,window=ll0)
                            canvas.create_window(120,50,window=ll1)
                            canvas.create_window(120,85,window=ll2)

                            q1=StringVar()
                            q2=StringVar()
                            w1=Entry(buy1,textvariable=q1)
                            w2=Entry(buy1,textvariable=q2)


                            canvas.create_window(230,50,window=w1)
                            canvas.create_window(230,85,window=w2)

                            def sub2():
                                try:
                                    add=q2.get()
                                    qua=q1.get()
                                    a=back1()
                        
                                    a.append(add)
                                    a.append(qua)

                                    cost=float(a[3])*int(a[6])
                                except:
                                    aqq='商城'
                                    bqq='输入的数量必须为数字！'
                                    eeer(aqq,bqq)
                                    return
                                #a[4]库存，a[6]购买数量
                                kkk=int(a[4])
                                a[6]=int(a[6])
                   
                          
                                #检查库存
                                if (kkk<a[6]):
                                    aa='商城'
                                    bb='库存不足！请检查购买数量！'
                                    eeer(aa,bb)
                                    return
                                else:
                                    a.append(cost)
                                    a.append(x)
                                    ddd=a[6]-kkk
                                    sql='insert into orders values("{}","{}","{}","{}","{}","{}","{}")'.format(x,a[0],a[1],a[2],add,qua,cost)
                                    cursor.execute(sql)
                                    db.commit()
                                    a[6]=kkk-a[6]
                                    ddd=int(a[6])
                               
                                    sql='update goods set num="{}" where gno="{}"'.format(a[6],a[1])
                                    cursor.execute(sql)
                                    db.commit()
                        

                                    buy1.destroy()

                                    aaaa='商城'
                                    bbbb='购买成功！'
                                    succ(aaaa,bbbb)
                                    #如果一次都买完了则从列表里删除该商品
                                    if ddd==0:
                                        theLB1.delete(ACTIVE)
                                    #如果在愿望单里，买完后从愿望单里删除
              
                                    sql='select * from wishlist where uname="{}" and gno="{}"'.format(x,a[1])
                                    cursor.execute(sql)
                                    ttt=cursor.rowcount
                                    if ttt==1:
                                        sql='delete from wishlist where uname="{}" and gno="{}"'.format(x,a[1])
                                        cursor.execute(sql)
                                        db.commit()
                                    return

                            Bb3=Button(buy1,text="立即下单",command=sub2)
                            canvas.create_window(200,130,window=Bb3)      
                        #添加到心愿单
                        def add1():
                            a=back1()
                            sql='select * from orders where gno="{}" and buyer="{}"'.format(a[1],x)
                            cursor.execute(sql)
                            if cursor.rowcount:
                                aqw='商城'
                                qwb='添加失败因为您已买到该商品喽~'
                                eeer(aqw,qwb)
                                return
                            sql='select * from wishlist where gno="{}" and uname="{}"'.format(a[1],x)
                            cursor.execute(sql)
                            if cursor.rowcount:
                                aqw='商城'
                                qwb='您已添加过该商品,请勿重复添加！'
                                eeer(aqw,qwb)
                                return

                            sql='insert into wishlist values("{}","{}","{}","{}","{}")'.format(x,a[0],a[1],a[2],float(a[3]))
                            cursor.execute(sql)
                            db.commit()
                            a='商城'
                            b='添加成功！'
                            succ(a,b)
                            return
                        Button(ss1,text="   买买买!!!   ",command=BuyBuyBuy1).grid(row=3,column=0)
                        Button(ss1,text="添加到心愿单",command=add1).grid(row=4,column=0)
                    return



                Bb3=Button(sou,text="   确定   ",command=chulai)
                canvas.create_window(140,50,window=ll3)
                canvas.create_window(200,110,window=Bb3)
                canvas.create_window(250,50,window=w1)



                Button(ss1,text="   买买买!!!   ",command=BuyBuyBuy)


                return
            theButton=Button(ss1,text="   买买买!!!   ",command=BuyBuyBuy)
            theButton.grid(row=3,column=0,sticky='w')
            theButton1=Button(ss1,text="添加到心愿单",command=add)
            theButton1.grid(row=3,column=0)
            Button(ss1,text='搜索商品',command=ser).grid(row=3,column=0,sticky='e')
        #查看我的宝贝
        def order():
            ord=Toplevel()
            ord.title('校园二手交易系统--我的宝贝')


            ord.update()
            w=ord.winfo_width()
            h=ord.winfo_height()
            ord.resizable(0,0)
            screenwidth = ord.winfo_screenwidth()
            screenheight = ord.winfo_screenheight()
            ord.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-650, (screenheight-h)/2-225))

            canvas = Canvas(ord,width=128,height=128,bd=0, highlightthickness=0)
            canvas.create_image(64,64, image=photo13)
            canvas.grid(row=0,column=0)

            orlbfr1=LabelFrame(ord,text='订单')
            orlbfr1.grid(row=1,column=0,padx=10,pady=10)

            orlbfr2=Frame(orlbfr1)
            orlbfr2.grid(row=0,column=0,padx=10,pady=10)

            Label(orlbfr2,anchor='w',text='卖家                                                             商品编号                                                        商品名称                                                       收货地址                                                        购买数量                                                       总金额',width=220).grid(row=0,column=0,sticky='W')
            theLB1 = Listbox(orlbfr2,setgrid=True,font=('YaHei Consolas Hybrid',12))#,selectmode=MULTIPLE
            theLB1.grid(row=2,column=0)
            theLB1.config(height=20,width=180)
                

            scrr=Scrollbar(orlbfr2)
            theLB1.config(yscrollcommand=scrr.set)
            scrr.config(command=theLB1.yview)
            scrr.grid(row=2,column=1,sticky='ns')

    
            sql='select seller,gno,gname,address,quantity,cost from orders where buyer="{}"'.format(x)
            cursor.execute(sql)

            #插入表的数据
            temp2=cursor.rowcount
            while temp2>0:
                t=cursor.fetchone()
                t=list(t)
                t[4]=str(t[4])
                t[5]=str(t[5])

                jk=[]
                for item in t:
                    cha=str(item)
                    leng=len(cha)
                    for item1 in cha:
                        if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                            leng+=1
                    while(leng<30):
                        cha=cha+' '
                        leng+=1
                    jk.append(cha)
                for item2 in [jk[0]+jk[1]+jk[2]+jk[3]+jk[4]+jk[5]]:
                        theLB1.insert(END,item2)
                temp2=temp2-1
                #返回选中的数据


            def back():
                b=list(theLB1.get(ACTIVE))
                #不赋初值之后会提示out of range
                mmm=0
                for each in b:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1
                c=[0,1,2,3,4,5]
                #表有6个项
                temp1=6
                k=0#指定c元素的位置
                k1=0#记录b元素的位置
                #每一项的第一个字
                c[0]=b[0]
                c[1]=b[30]
                c[2]=b[60]
                c[3]=b[90]
                c[4]=b[120]
                c[5]=b[150]
                while temp1:
                    fill1=29
                    #去空格
                    k1+=1
                    while fill1:
                        if b[k1]!=' ':
                            c[k]=c[k]+b[k1]
                            k1+=1
                            fill1-=1
                        else:
                            k1+=1
                            fill1-=1
                    k+=1
                    temp1-=1

                return c

            def shou():
                a=back()
                theLB1.delete(ACTIVE)
                sql='delete from orders where gno="{}"'.format(a[1]) 
                cursor.execute(sql)
                db.commit()
                a='我的订单'
                b='收货成功!'
                succ(a,b)
            def qu():
                aa=back()
                theLB1.delete(ACTIVE)
                sql='delete from orders where gno="{}"'.format(aa[1]) 
                cursor.execute(sql)
                db.commit()
                asd='我的订单'
                bsd='取消成功!'
                succ(asd,bsd)

            Button(orlbfr1,text="确认收货",command=shou).grid(row=1,column=0,padx=10,pady=5)
            Button(orlbfr1,text="取消订单",command=qu).grid(row=2,column=0,padx=10,pady=5)
        #查看我的心愿单
        def wish():
            ord=Toplevel()
            ord.title('校园二手交易系统--我的心愿单')

            ord.update()
            w=ord.winfo_width()
            h=ord.winfo_height()
            ord.resizable(0,0)
            screenwidth = ord.winfo_screenwidth()
            screenheight = ord.winfo_screenheight()
            ord.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-370, (screenheight-h)/2-225))

            canvas = Canvas(ord,width=64,height=64,bd=0, highlightthickness=0)
            canvas.create_image(32,32, image=photo14)
            canvas.grid(row=0,column=0)

            orlbfr1=LabelFrame(ord,text='心愿单')
            orlbfr1.grid(row=1,column=0,padx=10,pady=10)

            orlbfr2=Frame(orlbfr1)
            orlbfr2.grid(row=0,column=0,padx=10,pady=10)

            Label(orlbfr2,anchor='w',text='卖家                                                              商品编号                                                       商品名称                                                       单价',width=120).grid(row=0,column=0,sticky='W')
            theLB1 = Listbox(orlbfr2,setgrid=True,font=('YaHei Consolas Hybrid',12))
            theLB1.grid(row=2,column=0)
            theLB1.config(height=20,width=110)
                

            scrr=Scrollbar(orlbfr2)
            theLB1.config(yscrollcommand=scrr.set)
            scrr.config(command=theLB1.yview)
            scrr.grid(row=2,column=1,sticky='ns')

            sql='select seller,gno,gname,price from wishlist where uname="{}"'.format(x)
            cursor.execute(sql)

            #插入表的数据
            temp2=cursor.rowcount
            while temp2>0:
                t=cursor.fetchone()
                t=list(t)
                t[3]=str(t[3])

                jk=[]
                for item in t:
                    cha=str(item)
                    leng=len(cha)
                    for item1 in cha:
                        if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                            leng+=1
                    while(leng<30):
                        cha=cha+' '
                        leng+=1
                    jk.append(cha)
                for item2 in [jk[0]+jk[1]+jk[2]+jk[3]]:
                        theLB1.insert(END,item2)



                temp2=temp2-1
                #返回选中的数据

            def back():
                b=list(theLB1.get(ACTIVE))
                #不赋初值之后会提示out of range
                mmm=0
                for each in b:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1

                c=[0,1,2,3,4,5,6]
                temp1=4
                k=0#指定c元素的位置
                k1=0#记录b元素的位置
                #每一项的第一个字
                c[0]=b[0]
                c[1]=b[30]
                c[2]=b[60]
                c[3]=b[90]
                while temp1:
                    fill1=29
                    #去空格
                    k1+=1
                    while fill1:
                        if b[k1]!=' ':
                            c[k]=c[k]+b[k1]
                            k1+=1
                            fill1-=1
                        else:
                           k1+=1
                           fill1-=1
                    k+=1
                    temp1-=1
                return c

            def duo():
                #a[0]卖家,a[1]商品编号,a[2]商品名称,a[3]单价
                a=back()
                sql='select * from goods where gno="{}"'.format(a[1])
                cursor.execute(sql)
                if cursor.rowcount==0:
                    aaaaa='我的心愿单'
                    bbbbb='该商品已下架！'
                    eeer(aaaaa,bbbbb)
                    theLB1.delete(ACTIVE)
                    return
                qwe=cursor.fetchone()
                kuku=int(qwe[4])
                kukuinfo='当前库存:   {}'.format(kuku)

                #a[1]gno
                buy1=Toplevel()
                buy1.title('校园二手交易系统--商城')
                buy1.resizable(0,0)
                canvas = Canvas(buy1,width=400,height=180,bd=0, highlightthickness=0)
                canvas.create_image(50,50, image=photo11)
                canvas.grid(row=0,column=0)
                width=400
                heigh=180
                screenwidth = buy1.winfo_screenwidth()
                screenheight = buy1.winfo_screenheight()
                buy1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
                ll0=Label(buy1,text=kukuinfo)
                ll1=Label(buy1,text='购买数量:')
                ll2=Label(buy1,text='收货地址:')

                canvas.create_window(120,30,window=ll0)
                canvas.create_window(120,65,window=ll1)
                canvas.create_window(120,100,window=ll2)

                q1=StringVar()
                q2=StringVar()
                w1=Entry(buy1,textvariable=q1)
                w2=Entry(buy1,textvariable=q2)

                canvas.create_window(230,65,window=w1)
                canvas.create_window(230,100,window=w2)

                def xia():
                    try:
                        q=int(q1.get())#购买数量

                        add=q2.get()
                        a[4]=add#地址
                        a[5]=int(q)#数量
                        b=float(a[3])*float(q1.get())
                        a[6]=b#价格

                    except:
                        ppp='我的心愿单'
                        ooo='输入的数量必须为数字！'
                        eeer(ppp,ooo)
                        return

                    if q<kuku:
                        buy1.destroy()

                        sql='insert into orders values("{}","{}","{}","{}","{}","{}","{}")'.format(x,a[0],a[1],a[2],a[4],a[5],a[6])
                        
                        cursor.execute(sql)
                        db.commit()
                        theLB1.delete(ACTIVE)
                        sql='delete from wishlist where gno="{}"'.format(a[1]) 
                        cursor.execute(sql)
                        db.commit()
                        #修改数量
                        yyyyy=kuku-q

                        a[6]=yyyyy
                        sql='update goods set num="{}" where gno="{}"'.format(a[6],a[1])
                        cursor.execute(sql)
                        db.commit()


                        aa='我的心愿单'
                        b='剁手成功！'
                        succ(aa,b)
                        return
                    else:
                        vvv='我的心愿单'
                        nnn='库存不足！请检查购买数量！'
                        eeer(vvv,nnn)
                        return
                Bb3=Button(buy1,text="立即下单",command=xia)
                canvas.create_window(200,135,window=Bb3)
                return
            def shan():
                #a[0]卖家,a[1]商品编号,a[2]商品名称,a[3]单价
                a=back()
                sql='delete from wishlist where uname="{}" and gno="{}"'.format(x,a[1])
                cursor.execute(sql)
                db.commit()
                yui='我的心愿单'
                yui1='删除成功！'
                succ(yui,yui1)
                theLB1.delete(ACTIVE)
                return

            Button(ord,text="立即剁手",command=duo).grid(row=2,column=0,padx=10,pady=5)
            Button(ord,text="删除心愿",command=shan).grid(row=3,column=0,padx=10,pady=5)
        #查看我的商品
        def myPUB():
            new3=Toplevel()
            new3.title("校园二手交易系统--我的商品")

            new3.update()
            w=new3.winfo_width()
            h=new3.winfo_height()

            new3.resizable(0,0)
            screenwidth = new3.winfo_screenwidth()
            screenheight = new3.winfo_screenheight()
            new3.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-425, (screenheight-h)/2-295))

            canvas = Canvas(new3,width=1057,height=240,bd=0, highlightthickness=0)
            canvas.create_image(523,120, image=photo17)
            canvas.grid(row=0,column=0)

          
            ss1=LabelFrame(new3,text='商城')
            ss1.grid(row=1,column=0,padx=10,pady=10)

            ss2=Frame(ss1)
            ss2.grid(row=0,column=0,padx=10,pady=10)
            Label(ss2,anchor='w',text='商品编号                                                       商品名称                                                        单价                                                              库存',width=120).grid(row=0,column=0,sticky='W')

            theLB = Listbox(ss2,setgrid=True,font=('YaHei Consolas Hybrid',12))#,selectmode=MULTIPLE
            theLB.grid(row=2,column=0)
            theLB.config(height=20,width=110)

            scr=Scrollbar(ss2)
            theLB.config(yscrollcommand=scr.set)
            scr.config(command=theLB.yview)
            scr.grid(row=2,column=1,sticky='ns')

            sql='select * from goods where seller="{}"'.format(x)
            cursor.execute(sql)
            #插入表的数据
            temp2=cursor.rowcount
            while temp2>0:
                t=cursor.fetchone()
                t=list(t)
                t[3]=str(t[3])
                t[4]=str(t[4])

                jk=[]
                for item in t:
                    cha=str(item)
                    leng=len(cha)
                    for item1 in cha:
                        if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                            leng+=1
                    while(leng<30):
                        cha=cha+' '
                        leng+=1
                    jk.append(cha)
                for item2 in [jk[1]+jk[2]+jk[3]+jk[4]]:
                        theLB.insert(END,item2)
                temp2=temp2-1

            def back():
                b=list(theLB.get(ACTIVE))
                #不赋初值之后会提示out of range
                
                mmm=0
                for each in b:
                    if u'\u4e00' <= each <= u'\u9fa5':
                        b.insert(mmm+1,' ')
                        mmm+=1
                    else:
                        mmm+=1
                c=[0,1,2,3]
                #表有5个项
                temp1=3
                k=0#指定c元素的位置
                k1=0#记录b元素的位置
                #每一项的第一个字
                c[0]=b[0]
                c[1]=b[30]
                c[2]=b[60]
                c[3]=b[90]
                while temp1:
                    fill1=29
                    #去空格
                    k1+=1
                    while fill1:
                        if b[k1]!=' ':
                            c[k]=c[k]+b[k1]
                            k1+=1
                            fill1-=1
                        else:
                            k1+=1
                            fill1-=1
                    k+=1
                    temp1-=1
                sql='select * from goods where gno="{}"'.format(c[0])
                cursor.execute(sql)
                eee=cursor.fetchone()
                c.append(eee[4])
              
                return c
            def wu():
                a=back()
                #a[0]商品编号，a[1]商品名称，a[2]单价，a[4]库存
                sql='SET FOREIGN_KEY_CHECKS = 0'
                cursor.execute(sql)
                sql='delete from goods where gno="{}"'.format(a[0])
                cursor.execute(sql)
                db.commit()
                sql='SET FOREIGN_KEY_CHECKS = 1'
                cursor.execute(sql)
                theLB.delete(ACTIVE)
                yyy='我的商品'
                tyu='下架成功！'
                succ(yyy,tyu)
                return
            def bubu():
                
                pro=Toplevel()
                pro.title("校园二手交易系统--我的商品")
                w=291
                h=140
                pro.resizable(0,0)
                screenwidth = pro.winfo_screenwidth()
                screenheight = pro.winfo_screenheight()
                pro.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2, (screenheight-h)/2))
                canvas = Canvas(pro,width=w,height=h,bd=0, highlightthickness=0)

                canvas.create_image(40,60, image=photo16)
                canvas.grid(row=0,column=0)

                ll1=Label(pro,text='请输入商品数:')
                p1=StringVar()
                pro1=Entry(pro,textvariable=p1,width=15)

                canvas.create_window(130,55,window=ll1)
                canvas.create_window(230,55,window=pro1)
                
                def shang():
                    try:
                        a=back()
                        oo=int(p1.get())
                        oo=oo+int(a[4])
                        sql='update goods set num="{}" where gno="{}"'.format(str(oo),a[0])
                        cursor.execute(sql)
                        db.commit()
                        pro.destroy()
                        new3.destroy()
                        ghj='我的商品'
                        ghj1='补充成功！'
                        succ(ghj,ghj1)
                        return
                    except:
                        aaaa='我的商品'
                        bbbb='请输入数字！'
                        eeer(aaaa,bbbb)
                        return
            
                bbb=Button(pro,text="立即补货",command=shang)
                canvas.create_window(146,100,window=bbb)
            def myorder():
                ord=Toplevel()
                ord.title('校园二手交易系统--我的订单')

                ord.update()
                w=ord.winfo_width()
                h=ord.winfo_height()
                ord.resizable(0,0)
                screenwidth = ord.winfo_screenwidth()
                screenheight = ord.winfo_screenheight()
                ord.geometry('%dx%d+%d+%d'%(w, h, (screenwidth-w)/2-750, (screenheight-h)/2-225))

                canvas = Canvas(ord,width=128,height=128,bd=0, highlightthickness=0)
                canvas.create_image(64,64, image=photo13)
                canvas.grid(row=0,column=0)

                orlbfr1=LabelFrame(ord,text='订单')
                orlbfr1.grid(row=1,column=0,padx=10,pady=10)

                orlbfr2=Frame(orlbfr1)
                orlbfr2.grid(row=0,column=0,padx=10,pady=10)

                Label(orlbfr2,anchor='w',text='买家                                                             商品编号                                                        商品名称                                                       收货地址                                                        购买数量                                                        总金额',width=220).grid(row=0,column=0,sticky='W')
                theLB1 = Listbox(orlbfr2,setgrid=True,font=('YaHei Consolas Hybrid',12))
                theLB1.grid(row=2,column=0)
                theLB1.config(height=20,width=180)
                

                scrr=Scrollbar(orlbfr2)
                theLB1.config(yscrollcommand=scrr.set)
                scrr.config(command=theLB1.yview)
                scrr.grid(row=2,column=1,sticky='ns')

    
                sql='select * from orders where seller="{}"'.format(x)
                cursor.execute(sql)

                #插入表的数据
                temp2=cursor.rowcount
                while temp2>0:
                    t=cursor.fetchone()
                    t=list(t)
                    #t0买家t1卖家t2物品编号t3物品名称t4地址t5数量t6总花费
                    t[6]=str(t[6])
                    t[5]=str(t[5])
                    jk=[]
                    for item in t:
                        cha=str(item)
                        leng=len(cha)
                        for item1 in cha:
                            if u'\u4e00' <= item1 <= u'\u9fa5':#判断一个元素是否为汉字
                                leng+=1
                        while(leng<30):
                            cha=cha+' '
                            leng+=1
                        jk.append(cha)
                    for item2 in [jk[0]+jk[1]+jk[2]+jk[3]+jk[4]+jk[5]]:
                            theLB1.insert(END,item2)
                    temp2=temp2-1







            Button(new3,text="下架商品",command=wu).grid(row=2,column=0,padx=10,pady=5,sticky='w')
            Button(new3,text="补充商品",command=bubu).grid(row=2,column=0,padx=10,pady=5,sticky='n')
            Button(new3,text="我的订单",command=myorder).grid(row=2,column=0,padx=10,pady=5,sticky='e')

        uu1=Button(new1,width=15,text="发布商品",command=publish)
        uu2=Button(new1,width=15,text="游览商城",command=hang)
        uu3=Button(new1,width=15,text="心愿单",command=wish)
        uu4=Button(new1,width=15,text="我的宝贝",command=order)
        uu5=Button(new1,width=15,text="我的商品",command=myPUB)
        uu6=Button(new1,width=15,text="升级为管理员",command=promote)

        canvas.create_window(325,60,window=uu1)
        canvas.create_window(325,110,window=uu2)
        canvas.create_window(325,160,window=uu3)
        canvas.create_window(325,210,window=uu4)
        canvas.create_window(325,260,window=uu5)
        canvas.create_window(325,310,window=uu6)
    return



#用户注册
def create_register():
    top=Toplevel()
    top.title("校园二手交易系统--注册")
    width=253
    heigh=300
    top.resizable(0,0)
    screenwidth = top.winfo_screenwidth()
    screenheight = top.winfo_screenheight()
    top.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

    canvas = Canvas(top,width=253,height=300,bd=0, highlightthickness=0)
    canvas.create_image(126,51, image=photo2)
    canvas.grid(row=0,column=0)



    bb1=Label(top,text='账号:')
    bb2=Label(top,text='用户名:')
    bb3=Label(top,text='密码:')
    canvas.create_window(66,140,window=bb1)
    canvas.create_window(60,170,window=bb2)
    canvas.create_window(66,200,window=bb3)

    t1=StringVar()
    t2=StringVar()
    t3=StringVar()

    r1=Entry(top,width=17,textvariable=t1)
    r2=Entry(top,width=17,textvariable=t2)
    r3=Entry(top,width=17,textvariable=t3,show='*')
    canvas.create_window(160,140,window=r1)
    canvas.create_window(160,170,window=r2)
    canvas.create_window(160,200,window=r3)

    def register():
        uid=t1.get()
        uname=t2.get()
        password=t3.get()
        #查询数据库中账号是否已经被注册
        sql='select uid from user where uid="{}"'.format(uid)
        cursor.execute(sql)
        if cursor.rowcount:
            a='注册'
            b='该账号已被注册！请重新选择一个账号！'
            eeer(a,b)
            return
        #查询数据库中用户名是否已被注册
        sql='select uname from user where uname="{}"'.format(uname)
        cursor.execute(sql)
        if cursor.rowcount:
            a='注册'
            b='该用户名已被注册！请重新选择一个用户名！'
            eeer(a,b)
            return
        try:
            sql='insert into user values("{}","{}","{}","{}")'.format(uid,uname,password,0)
            cursor.execute(sql)
            db.commit()
            #注册成功弹窗
            a='注册'
            b='恭喜您~注册成功啦！'
            succ(a,b)
            top.destroy()
        except:
            a='注册'
            b='啊哦~注册失败！字符长度超过最大限制！'
            eeer(a,b)
        return
    bb1=Button(top,text='立即注册',command=register)
    canvas.create_window(126,250,window=bb1)
    return

#基本用户界面
root=Tk()
root.title("校园二手交易系统")
root.resizable(0,0)
#窗口居中
width=537
heigh=617

#获取屏幕大小
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

#设置画布
canvas00 = Canvas(root,width=537,height=617,bd=0, highlightthickness=0)
#设置图片
imgpath = '2.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas00.create_image(268, 308, image=photo)#(图片长度除2，图片宽度除2)
canvas00.grid(row=0,column=0)

#登录窗口背景定义处
imgpath1= 'welcome.gif'
img1= Image.open(imgpath1)
photo1= ImageTk.PhotoImage(img1)
#注册窗口背景定义处
imgpath2= 'join.gif'
img2= Image.open(imgpath2)
photo2= ImageTk.PhotoImage(img2)
#错误提醒背景图片定义处
imgpath3= '错误.gif'
img3= Image.open(imgpath3)
photo3= ImageTk.PhotoImage(img3)
#成功提醒图片定义处
imgpath4= '正确.gif'
img4= Image.open(imgpath4)
photo4= ImageTk.PhotoImage(img4)
#用户背景定义处
imgpath5= '背景.gif'
img5= Image.open(imgpath5)
photo5= ImageTk.PhotoImage(img5)
#发布商品窗口背景
imgpath6= '上.gif'
img6= Image.open(imgpath6)
photo6= ImageTk.PhotoImage(img6)

imgpath7= '中左.gif'
img7= Image.open(imgpath7)
photo7= ImageTk.PhotoImage(img7)

imgpath8= '中右.gif'
img8= Image.open(imgpath8)
photo8= ImageTk.PhotoImage(img8)

imgpath9= '下.gif'
img9= Image.open(imgpath9)
photo9= ImageTk.PhotoImage(img9)
#升级为管理员背景定义处
imgpath10= '管理.gif'
img10= Image.open(imgpath10)
photo10= ImageTk.PhotoImage(img10)
#下单图片
imgpath11= '订单.gif'
img11= Image.open(imgpath11)
photo11= ImageTk.PhotoImage(img11)
#商城背景
imgpath12= 'nice.gif'
img12= Image.open(imgpath12)
photo12= ImageTk.PhotoImage(img12)
#我的订单背景
imgpath13= 'smile.gif'
img13= Image.open(imgpath13)
photo13= ImageTk.PhotoImage(img13)
#我的心愿单背景
imgpath14= 'wish.gif'
img14= Image.open(imgpath14)
photo14= ImageTk.PhotoImage(img14)
#管理员
imgpath15= 'admin.gif'
img15= Image.open(imgpath15)
photo15= ImageTk.PhotoImage(img15)
#补货
imgpath16= '补货.gif'
img16= Image.open(imgpath16)
photo16= ImageTk.PhotoImage(img16)
#我的商品
imgpath17= '球.gif'
img17= Image.open(imgpath17)
photo17= ImageTk.PhotoImage(img17)
#商品
imgpath18= '商品.gif'
img18= Image.open(imgpath18)
photo18= ImageTk.PhotoImage(img18)
#改密码
imgpath19= '密码.gif'
img19= Image.open(imgpath19)
photo19= ImageTk.PhotoImage(img19)

bb1=Button(root,text='登录',command=new)
bb2=Button(root,text='注册',command=create_register)
bb3=Button(root,text='退出',command=root.destroy)



canvas00.create_window(268,238,width=100, height=50,window=bb1)
canvas00.create_window(268,308,width=100, height=50,window=bb2)
canvas00.create_window(268,378,width=100, height=50,window=bb3)

root.mainloop()