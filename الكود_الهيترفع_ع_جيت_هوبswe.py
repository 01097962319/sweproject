from tkinter import*  # استيراد كل العناصر من مكتبة Tkinter
from tkinter import ttk  # استيراد العناصر المخصصة من مكتبة ttk
from tkcalendar import DateEntry  # استيراد DateEntry من مكتبة tkcalendar


root=Tk()  # إنشاء نافذة التطبيق الرئيسية
root.geometry("470x340",)  # تعيي أبعاد النافذة
root.title("Data Entry Form")  # تعيين عنوان النافذة
root.background(000814)
######################################
title = Label(root, text="Data Entry Form", font="calibre 20 bold",fg="red")  #لون النص و نشاء تسمية العنوان وتعيين الخط
title.grid(row=0, column=0, pady=10, columnspan=4)  # وضع التسمية في الشبكة (grid)

############################################....FirstName......
fname = Label(root, text="FirstName")  # إنشاء تسمية للاسم الأول
fname.grid(row=1, column=0)  # وضع التسمية في الشبكة
FirstNameinput = Entry(root, width=20)  # إنشاء حقل إدخال للاسم الأول
FirstNameinput.grid(row=1, column=1)  # وضع حقل الإدخال في الشبكة

############################################....LastName........
lname = Label(root, text="LastName")  # إنشاء تسمية للاسم الأخير
lname.grid(row=1, column=2)  # وضع التسمية في الشبكة
LastNameinput = Entry(root, width=20)  # إنشاء حقل إدخال للاسم الأخير
LastNameinput.grid(row=1, column=3)  # وضع حقل الإدخال في الشبكة

#############################################......birth day............
birthday = Label(root, text="BirthDay")  # إنشاء تسمية لتاريخ الميلاد
birthday.grid(row=2, column=0)  # وضع التسمية في الشبكة
birthdayinput = DateEntry(root, width=55)  # إنشاء حقل إدخال لتاريخ الميلاد باستخدام DateEntry
birthdayinput.grid(row=2, column=1, columnspan=4, pady=10)  # وضع حقل الإدخال في الشبكة

##################################################........gender..............
gender = Label(root, text="gender")  # إنشاء تسمية للجنس
gender.grid(row=3, column=0)  # وضع التسمية في الشبكة
gender = StringVar()  # إنشاء متغير StringVar لتخزين قيمة الجنس
gender.set("none")  # تعيين القيمة الابتدائية لمتغير الجنس
male = Radiobutton(root, text="Male", value="Male", variable=gender)  # إنشاء زر اختيار للجنس (ذكر)
male.grid(row=3, column=1, pady=10)  # وضع زر الاختيار في الشبكة

fmale = Radiobutton(root, text="Female", value="Female", variable=gender)  # إنشاء زر اختيار للجنس (أنثى)
fmale.grid(row=3, column=3, pady=10)  # وضع زر الاختيار في الشبكة

##################################################.........country.....................
country = Label(root, text="Country")  # إنشاء تسمية للبلد
country.grid(row=4, column=0)  # وضع التسمية في الشبكة
countryinput = ttk.Combobox(root, width=55, values=["EGYPT", "SYRIA", "SAUDI ARABIC", "QATAR", "IRAQ", "SUDAN", "ALGERIA", "MOROCCO"])  # إنشاء قائمة منسدلة للبلدان
countryinput.grid(row=4, column=1, columnspan=4)  # وضع القائمة المنسدلة في الشبكة

###################################################............address......................
adress = Label(root, text="address")  # إنشاء تسمية للعنوان
adress.grid(row=5, column=0, padx=10)  # وضع التسمية في الشبكة
adressinput = Entry(root, width=60)  # إنشاء حقل إدخال للعنوان
adressinput.grid(row=5, column=1, columnspan=4, pady=10)  # وضع حقل الإدخال في الشبكة

##############################################################..............Button.and.function..................
def fun():  # دالة لحفظ البيانات المدخلة
    FirstName = FirstNameinput.get()  # جلب قيمة الاسم الأول
    LastName = LastNameinput.get()  # جلب قيمة الاسم الأخير
    birthday = birthdayinput.get()  # جلب قيمة تاريخ الميلاد
    gender_value = gender.get()  # جلب قيمة الجنس
    country = countryinput.get()  # جلب قيمة البلد
    adress = adressinput.get()  # جلب قيمة العنوان
    text = FirstName + "," + LastName + "," + birthday + "," + gender_value + "," + country + "," + adress + "\n"  # دمج القيم في نص واحد

    with open(r"E:\عمليات\swe.csv", "+a") as file:  # فتح الملف في وضع الإضافة
        file.write(text)  # كتابة النص في الملف

#**************************************************
def clear():  # دالة لمسح البيانات المدخلة
    FirstNameinput.delete(0, "end")  # مسح قيمة الاسم الأول
    LastNameinput.delete(0, "end")  # مسح قيمة الاسم الأخير
    birthdayinput.delete(0, "end")  # مسح قيمة تاريخ الميلاد
    gender.set("none")  # إعادة تعيين قيمة الجنس
    countryinput.set('')  # مسح قيمة البلد
    adressinput.delete(0, "end")  # مسح قيمة العنوان
   
save = Button(root, text="Save", font=("Helvetica", 12), command=fun)  # إنشاء زر الحفظ وربط دالة fun به
save.grid(row=6, column=1)  # وضع زر الحفظ في الشبكة

clear = Button(root, text="Clear", font=("Helvetica", 12), command=clear)  # إنشاء زر المسح وربط دالة clear به
clear.grid(row=6, column=2)  # وضع زر المسح في الشبكة

root.mainloop()  # بدء الحلقة الرئيسية لتشغيل التطبيق

