#แสดงข้อมูลหลายๆ ประเภทใน Print เดียว
#1. ใช้ , โดยจะมี space ในแต่ละ ,
print("SAU",555,123.456,True,10+50)

#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช่ string ต้องแปลงเป็น String และไม่มี space ให้เหมือนกับ ,
print("SAU"+str(555)+str(123.456)+str(True)+str(10+50))
print("SAU "+str(555)+' '+str(123.456)+' '+str(True)+' '+str(10+50))

#3. ใช้เมธอตชื่อ format
print("SAU {} {} {} {}".format(555, 123.456, True, 10+50))
print("SAU {0} {1} {3} {2}".format(555, 123.456, True, 10+50))

#4. ใช้ f-string ***
print(f'SAU {555} {123.456} {True} {10+50}')

#---------------------
#กรณี 1 บรรทัดมีหลาย Statment ให้คั่นด้วย ;
print('aaa'); print(111); print(False)

