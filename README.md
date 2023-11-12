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
