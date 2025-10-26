# Nexus 聊天機器人

這是一個以 **NLTK** 與 **Gradio** 製作的簡易中文聊天機器人。  
它能夠進行基本的文字對話，支援中文分詞與常見互動，並以網頁介面運行。

---

## 📦 環境需求

在執行程式前，請先安裝必要套件：

```bash
!pip install gradio
```

另外，程式中會自動下載 NLTK 所需資源 (`punkt`)，首次執行時可能需要一些時間。

---

## 🧠 主要技術

- **NLTK**：用於簡單規則式對話（`Chat` 與 `reflections`）。
- **jieba**：中文斷詞工具。
- **Gradio**：建立互動式網頁聊天介面。

---

## 🚀 執行方式

1. 下載並開啟 `nexus_聊天機器人.py`
2. 在終端機或 Jupyter Notebook 中執行：
   ```bash
   python nexus_聊天機器人.py
   ```
3. 終端機會顯示一個網址（或自動開啟網頁），即可開始與聊天機器人互動。

---

## 🗂️ 檔案結構

```
nexus_聊天機器人.py   # 主程式，包含聊天邏輯與Gradio介面
README.md              # 使用說明文件
```

---

## 💬 範例互動

| 使用者輸入 | 機器人回覆 |
|-------------|-------------|
| 你好 | 嗨！很高興見到你！ |
| 你叫什麼名字 | 我是你的AI朋友，叫我Nexus就好。 |
| 我心情不好 | 深呼吸，一切都會好起來的。 |
| 再見 | 下次再聊！ |

---

## 📚 延伸改進建議

- 增加自定義語料或情緒辨識功能  
- 使用大型語言模型替換規則式回覆  
- 整合資料庫保存對話紀錄
---
# Nexus Chatbot

This is a simple Chinese chatbot built with **NLTK** and **Gradio**.  
It can perform basic text conversations, supports Chinese word segmentation, and runs through a web interface.

---

## 📦 Requirements

Before running the program, install the required package:

```bash
!pip install gradio
```

The script will automatically download the necessary NLTK resource (`punkt`) during the first run, which may take a few moments.

---

## 🧠 Core Technologies

- **NLTK**: Used for simple rule-based chatting (`Chat` and `reflections`).
- **jieba**: Chinese word segmentation tool.
- **Gradio**: Creates an interactive web chat interface.

---

## 🚀 How to Run

1. Download and open `nexus_聊天機器人.py`
2. Run the following command in your terminal or Jupyter Notebook:
   ```bash
   python nexus_聊天機器人.py
   ```
3. A web link will appear in the terminal (or open automatically).  
   Use it to start chatting with the bot.

---

## 🗂️ File Structure

```
nexus_聊天機器人.py   # Main program with chatbot logic and Gradio interface
README_EN.md          # English documentation file
```

---

## 💬 Example Conversation

| User Input | Bot Reply |
|-------------|-----------|
| 你好 | Hi! Nice to meet you! |
| 你叫什麼名字 | I’m your AI friend, call me Nexus. |
| 我心情不好 | Take a deep breath, everything will be fine. |
| 再見 | See you next time! |

---

## 📚 Possible Improvements

- Add custom datasets or emotion recognition  
- Replace rule-based responses with a large language model  
- Store chat history in a database
