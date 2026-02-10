import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import threading
import subprocess
import os

# --- НАСТРОЙКИ ---
MIC_INDEX = 0      # Поменяй, если в списке в терминале твой микрофон под другим номером
SENS_X, SENS_Y = 2.5, 3.5
OFFSET_X, OFFSET_Y = 0.5, 0.5
SMOOTH = 0.15
curr_x, curr_y = 0, 0

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# Вывод списка микрофонов при старте
print("Доступные микрофоны:")
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"[{i}] {name}")

def voice_control():
    rec = sr.Recognizer()
    rec.energy_threshold = 500 # Чувствительность к голосу
    
    with sr.Microphone(device_index=MIC_INDEX) as source:
        while True:
            try:
                print(">>> Слушаю...")
                audio = rec.listen(source, phrase_time_limit=4)
                cmd = rec.recognize_google(audio, language="ru-RU").lower()
                print(f"Услышал: {cmd}")

                if "ворд" in cmd or "word" in cmd or "открой" in cmd:
                    print("Запуск Word...")
                    # Пытаемся запустить через PowerShell (самый надежный метод)
                    subprocess.Popen(["powershell", "Start-Process winword"], shell=True)
                
                elif "напечатай" in cmd:
                    import pyperclip
                    import time
                    
                    # Очищаем текст от команды
                    text_to_print = cmd.replace("напечатай", "").strip()
                    
                    if text_to_print:
                        print(f"Готовлюсь напечатать: {text_to_print}")
                        pyperclip.copy(text_to_print)
                        
                        # Даем тебе время подготовиться
                        print("ВНИМАНИЕ: Сейчас будет произведен КЛИК и ВСТАВКА...")
                        time.sleep(2)
                        
                        # 1. ПРИНУДИТЕЛЬНЫЙ КЛИК в текущее место курсора (где твой взгляд)
                        # Это заставляет Windows переключить фокус именно туда, куда ты смотришь
                        pyautogui.click()
                        time.sleep(0.5)
                        
                        # 2. ВСТАВКА через зажатие клавиш (более надежно, чем hotkey)
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        
                        print("Текст успешно вставлен!")
                    
                    text = cmd.replace("напечатай", "").strip()
                    if text:
                        print(f"Подготовка к печати: {text}")
                        # Копируем текст в буфер
                        pyperclip.copy(text)
                        
                        # ДАЕМ ПАУЗУ 3 СЕКУНДЫ
                        # В это время ты должна ГЛАЗАМИ (морганием) нажать на лист Word
                        print("У тебя 3 секунды, чтобы активировать окно Word!")
                        time.sleep(3)
                        
                        # Эмулируем нажатие Ctrl+V через более низкоуровневую команду
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        print("Команда вставки отправлена.")
                    
                    if text:
                        print(f"Попытка прямой печати: {text}")
                        # 1. Даем паузу, чтобы ты успела моргнуть в Word
                        pyautogui.sleep(2.0)
                        
                        # 2. Печатаем текст напрямую (убедись, что раскладка РУС)
                        import pydirectinput # Если её нет, напиши pip install pydirectinput
                        pyautogui.write(text, interval=0.1) 
                        
                        # 3. Если всё равно не пишет, попробуем нажать Enter в конце
                        pyautogui.press('enter')
                    
                    if text:
                        print(f"Копирую в буфер и вставляю: {text}")
                        # 1. Копируем текст в буфер обмена Windows
                        pyperclip.copy(text)
                        
                        # 2. Ждем чуть-чуть, чтобы ты успела сфокусировать взгляд
                        pyautogui.sleep(0.5)
                        
                        # 3. Эмулируем нажатие Ctrl + V (вставить)
                        pyautogui.hotkey('ctrl', 'v')
                    
            except:
                pass

# Запуск голоса в фоне
threading.Thread(target=voice_control, daemon=True).start()

# Eye Tracking
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    success, frame = cam.read()
    if not success: break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    
    if output.multi_face_landmarks:
        landmarks = output.multi_face_landmarks[0].landmark
        iris = landmarks[473] # Точка зрачка
        
        # Расчет и сглаживание
        target_x = screen_w * ((iris.x - OFFSET_X) * SENS_X + 0.5)
        target_y = screen_h * ((iris.y - OFFSET_Y) * SENS_Y + 0.5)
        curr_x += (target_x - curr_x) * SMOOTH
        curr_y += (target_y - curr_y) * SMOOTH
        
        pyautogui.moveTo(max(0, min(screen_w, curr_x)), max(0, min(screen_h, curr_y)))

        # Клик (левый глаз)
        left = [landmarks[145], landmarks[159]]
        if (left[0].y - left[1].y) < 0.012:
            pyautogui.click()
            pyautogui.sleep(0.4)

    cv2.putText(frame, "EyeDrive + Voice Active", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('EyeDrive Presentation', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
