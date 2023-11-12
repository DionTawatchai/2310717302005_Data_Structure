# 2310717302005_Data_Structure
2310717302005_UTCC_Tawatchai_Treerapagon_Data_Structure
## Assignment 2: Stacks and Queues
- จากโจทย์จงใช้ Unit Test (ไฟล์ที่แนบมานี้)ในการทดสอบอัลกอริทึมในการตรวจจับเครื่องหมายให้ผ่านอย่างน้อย 4 Test Cases จากทั้งหมด 5 Test Cases
* คะแนนพิเศษ (10 คะแนน) - Optional ให้ปรับปรุงอัลกอริทึมจนสามารถผ่านทั้ง 5 Test Cases ได้ 
* อธิบายกลไกของอัลกอริทึม การทดสอบ และรูปผลการทดสอบ Unit Test 
- ไฟล์ที่ชื่อว่า Stack.py
    - จะเป็น class เพื่อเรียกใช้ คำสั่งดังต่อไปนี้
      - isEmpty()
        - คือ ฟังก์ชั่นเช็ค ว่าใน list เป็นค่าว่างหรือไหม
      - push()
        - คือ การนำ Data เข้า 
      - pop()
        - คือ การนำ Data Delete ออก
      - size()
        - คือ ฟังก์ชั่น ที่วัด จำนวน ว่ามีตัวใน list
  
- ไฟล์ที่ชื่อว่า bracket_check1.py
    - คือ ชุดคำสั่ง ที่ใช้ check bracket ว่า มีครบคู่ไหม ตัวอย่างเช่น () , {} , [] ถ้าไม่ครบคู่ก็จะแสดงออกมาว่าผิดที่ตำแหน่งใด

  code
      
      from Stack import Stack #ทำการimport ไฟล์ Stack เพื่อใช้งานฟังก์ชั่น

        def bracket_check(test_string):
            stack = Stack() #ทำการเรียกใช้ constructor 
            opening_brackets = "({[" #ทำการเก็บค่าตัวแปร จำพวก bracket เปิด
            closing_brackets = ")}]" #ทำการเก็บค่าตัวแปร จำพวก bracket ปิด

            is_error = False #ทำการset ค่าตัวแปร is_error เป็น False
            location = [] #ทำการset ค่าตัวแปร location เป็น list ว่างๆ

            for i in range(len(test_string)): #ทำการวน loop โดยเริ่มจาก 0 ไปถึงจน จำนวนที่นับค่าได้ใน test_string
                char = test_string[i] #กำหนด เก็บค่าstring ของ ตัวแปร test_string ตัวที่ i ที่วนไปเรื่อยๆ ลงค่าตัวแปร char 

                if char in opening_brackets: #ทำการวน loop เช็ค ว่ามีbracket เปิดใน opening_bracketsไหม
                    stack.push((char, i)) #ทำการ push data โดยเรียกใช้จากไฟล์ stack

                elif char in closing_brackets: #ทำการวน loop เช็ค ว่ามี bracket ปิดใน closing_brackets
                    if stack.isEmpty(): #ทำการเช็คว่า เป็น list ว่างไหม โดยเรียกใช้จากไฟล์ Stack
                        is_error = True #ถ้าทำการเช็คว่า เป็น list ว่าง ให้set ค่า is_error เป็น True
                        location.append(i) #ทำการเพิ่มตำแหน่งที่ i ไปยัง location
                    else:#ถ้าไม่เป็น list ว่าง
                    top, idx = stack.pop() #ทำการ pop ออก โดยเรียกใช้จาก Stack
                    if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):#ทำการcheck เงื่อนไข
                        is_error = True #ทำการset ค่าตัวแปร is_error เป็น True
                        location.append(i)#ทำการเพิ่มตำแหน่งที่ i ไปยัง location
                        break #ทำการหยุด

            if not stack.isEmpty(): #ถ้าไม่เป็น list ว่าง
                is_error = True #ทำการset ค่าตัวแปร is_error เป็น True
                while not stack.isEmpty():
                    top, idx = stack.pop() #ทำการ pop ออก โดยเรียกใช้จาก Stack
                    location.append(idx) #ทำการเพิ่มตำแหน่งที่ idx ไปยัง location

            return is_error, location #ส่งออกค่า is_error และ location
        test_string = '{}{' # กำหนดค่าตัวแปรเพื่อใช้ในการ test ตรวจสอบว่า bracket ครบไหม
        isError, locations = bracket_check(test_string) #เก็บค่า ลง isError และ locations และเรียกใช้ฟังก์ชั่น bracket_check()
        print(f'error: {isError}') #ทำการแสดงค่า isError
        print('location:', locations) #ทำการแสดงค่า locations

![Bracket_test](https://github.com/DionTawatchai/2310717302005_Data_Structure/assets/150526207/ab4ec3d4-dc04-40af-bd4a-57d0e9d0a59c)

  
- ไฟล์ที่ชื่อว่า test_bracket_1.py
    - คือ ชุดคำสั่ง unitest เพื่อใช้ทดสอบความถูกต้องของ code ของไฟล์ bracket_check1.py ว่าผลจะRun อออกมาได้ถูกต้องหรือไม่
      - โดย หลักการทำงานของ ไฟล์นี้ คือ มีฟังก์ชั่น test อยู่ 5 test case
     
  
  def test_no_error(self):
  
      def test_no_error(self):
        test_string = '[{(Hello)}]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, False)

      คือ การ check string คำว่า [{(Hello)}] ว่ามี bracket ครบไหม และ คาดว่า ผลจะออกมาเป็น False

  def test_error_1(self):
  
      def test_error_1(self):
        test_string = '[{(Hello})]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
  
      คือ การ check string คำว่า [{(Hello})] ว่ามี bracket ครบไหม และ คาดว่า ผลจะออกมาเป็น True
  
  def test_error_2(self):
  
      def test_error_2(self):
        test_string = '[{(Hello'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
  
      คือ การ check string คำว่า [{(Hello ว่ามี bracket ครบไหม และ คาดว่า ผลจะออกมาเป็น True

  def test_error_3(self):

      def test_error_3(self):
        test_string = 'Hello)('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
  
      คือ การ check string คำว่า [{(Hello ว่ามี bracket ครบไหม และ คาดว่า ผลจะออกมาเป็น True
  
  def test_error_4(self):

      def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        self.assertEqual(location, [2])
        
      คือ การ check string คำว่า {}{ ว่ามี bracket ครบไหม และ คาดว่า ผลจะออกมาเป็น True และผิดพลาดที่ ตำแหน่ง [2]

ผลลัพธ์การ Run Code ที่ทำการเช็ค Unitest (test_bracket_check_1) กับ ไฟล์ bracket_check_1 

    ผลสรุปได้ว่าสามารถ Test คำสั่งได้ 5 Test case จากโจทย์ สามารถตรวจสอบได้ถูกต้องทั่งหมด
![Unitest1](https://github.com/DionTawatchai/2310717302005_Data_Structure/assets/150526207/ee892dcb-3539-4697-9b8d-1613ac212639)


