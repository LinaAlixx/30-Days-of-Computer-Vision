import os

def create_challenge_folders():
    # تكرار من 1 إلى 30
    for i in range(1, 31):
        # تنسيق الرقم ليكون بخانتين (01, 02, ... 30)
        day_str = f"{i:02d}"
        folder_name = f"Day_{day_str}"
        
        # إنشاء المجلد (لن يقوم بالكتابة فوقه إذا كان موجوداً مسبقاً بفضل exist_ok)
        os.makedirs(folder_name, exist_ok=True)
        
        # محتوى ملف README الفرعي لكل يوم
        readme_content = f"""# Day {i}: [Topic Title] 🖼️

## 📝 Project Overview
Add a brief description of what you accomplished in Day {i}.

## 🛠️ Tech Stack
- Python 3.x
- OpenCV (`cv2`)

## 🧠 Key Learnings
1. 
2. 
3. 

## 💻 How to Run
```bash
cd {folder_name}
# Run your script here
python script.py
