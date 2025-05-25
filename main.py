import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

# 页面配置
st.set_page_config(
    page_title="💬克隆ChatGPT",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💬克隆ChatGPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")
    
    # 在左边侧边栏放按钮
    if st.button("🔄 重新开始会话"):
        st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = [{"role": "ai", "content": "您好，我是您的AI小助手，有什么可以帮到您哒？"}]
        st.rerun()  # 立即刷新页面

# 初始化会话状态
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai", "content": "您好，我是您的AI小助手，有什么可以帮到您哒？"}]

# 显示聊天历史
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 处理用户输入
prompt = st.chat_input("请输入您的问题...")
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API密钥")
        st.stop()
    
    # 添加用户消息
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    # 获取AI回复
    with st.spinner("AI正在思考中，请稍等……"):
        try:
            response = get_chat_response(prompt, st.session_state["memory"], openai_api_key)
            msg = {"role": "ai", "content": response}
            st.session_state["messages"].append(msg)
            st.chat_message("ai").write(response)
        except Exception as e:
            error_msg = f"抱歉，发生了错误：{str(e)}"
            st.error(error_msg)
            st.session_state["messages"].append({"role": "ai", "content": error_msg})

