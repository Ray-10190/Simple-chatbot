import nltk
import jieba
import gradio as gr
from nltk.chat.util import Chat, reflections

# 下載必要的NLTK資源
nltk.download('punkt')

# 定義處理用戶輸入的函數
def respond(message, history):
    # 使用jieba進行中文分詞
    words = jieba.cut(message)
    # 將分詞後的結果組合成字符串
    processed_message = " ".join(words)
    # 獲取聊天機器人的回應
    response = chatbot.respond(processed_message)
    return response

pairs = [

    [
        r"你好|嗨|哈囉",
        ["你好！", "嗨！很高興見到你！", "哈囉！有什麼我可以幫你的嗎？"]
    ],
    [
        r"你叫什麼名字",
        ["我是一個AI聊天機器人，你可以叫我Nexus。", "我是你的AI朋友，叫我Nexus就好。", "你可以叫我Nexus"]
    ],
    [
        r"再見|拜拜",
        ["再見！", "下次再聊！", "祝你有個愉快的一天！"]
    ],
    [
        r".*",
        ["對不起,我不懂你的意思"]
    ],
    # 感情相關
    [
        r"我心情不好",
        ["心情不好是正常的，有什麼我可以為你做的嗎？", "深呼吸，一切都會好起來的。", "跟我聊聊吧，也許會讓你感覺好一點。"]
    ],
    [
        r"我很開心",
        ["很高興聽到你開心！", "有什麼開心的事情可以跟我分享嗎？", "保持好心情，生活會更美好。"]
    ],
    # 開玩笑
    [
        r"講個笑話",
        ["媽媽指著食人魚跟女兒說：「女兒，你看，這是會吃人的魚。」而食人魚媽媽則跟食人魚女兒說：「女兒，你看，這是會吃魚的人。」"]
    ],

    # 其他
    [
        r"謝謝",
        ["不客氣！", "能為您服務是我的榮幸。"]
    ],
    [
        r"對不起",
        ["沒關係，大家都會犯錯。", "不用道歉，我們繼續聊吧。"]
    ]
]

# 創建聊天機器人
chatbot = Chat(pairs, reflections)

# 創建Gradio界面
iface = gr.ChatInterface(
    respond,
    title="Nexus聊天機器人",
    description="這是一個使用NLTK和Gradio創建的聊天機器人。",
    theme="soft"
)

# 啟動Gradio界面
iface.launch(share=True)