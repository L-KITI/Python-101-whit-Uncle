s=0
i=0
while True:
    n= int(input("input you number : "))
    if n==0:
        break
    s+=n
    i+=1
print("จำนวนจ้อมูลทั้งหมด",i)
print("ค่าเฉลี่ย = ",s/i)
print("จบโปรแกรม.")
