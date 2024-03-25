import time
import pyautogui
import winsound

# 实现WPS实现表格自动输入和保存
sleeptime = 0.0005
time.sleep(2)  # 等待，单位是s；用于启动并最小化py脚本程序
# 本电脑分辨率 1920*1080
for x in range(1,4):  # x小于26
    for y in range(1,4): # y小于43,不要超过屏幕
        x1 = round(69.23*x-69.23+70)
        pX = str(x1)
        y1 = round(18*y-18+220)
        pY = str(y1)
        input_txt = str(x1)+'-'+str(y1)

        # 鼠标单击左键，xy是鼠标单击坐标
        pyautogui.click(x1, y1) # wps表格对应的像素位置
        # 等待，单位是s
        time.sleep(sleeptime)

        # 键盘输入，字符串
        pyautogui.typewrite(input_txt)   # 输入字符串
        time.sleep(sleeptime)

# 另存为
pyautogui.click(48, 58)
time.sleep(sleeptime)
pyautogui.click(81, 231)
time.sleep(sleeptime)
pyautogui.click(306, 465)
time.sleep(sleeptime)

# 文件名
pyautogui.click(663, 539)
time.sleep(sleeptime)
pyautogui.doubleClick(798, 570)
time.sleep(sleeptime)
pyautogui.click(871, 850)
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'a') # ctrl+a全选按下
time.sleep(sleeptime)
#pyautogui.keyUp('ctrl','a') # ctrl+a全选松开
#time.sleep(sleeptime)

file_name = 'auto-office-A-M0001'  # 中文输入法时，文件名里面不要带有数字
time.sleep(0.1)   
# 键盘输入，字符串
pyautogui.typewrite(file_name)   # 输入字符串
#pyautogui.hotkey('1') # 中文输入法时，输入后要选择序号
# 等待，单位是s
time.sleep(0.1)

# 保存文件
pyautogui.click(1384, 920)
time.sleep(0.1)

# 电脑蜂鸣器发声，参数分别是频率（赫兹）和持续时间（毫秒）
winsound.Beep(1000, 1000)