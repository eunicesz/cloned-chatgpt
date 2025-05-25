# 💬 克隆ChatGPT

一个基于Streamlit和LangChain的ChatGPT克隆应用。

## 功能特点

- 🤖 支持GPT-3.5-turbo模型
- 💬 实时对话界面
- 🔄 会话重置功能
- 📱 响应式设计
- 🔐 API密钥安全输入

## 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
streamlit run main.py
```

3. 在浏览器中打开 `http://localhost:8501`

## Streamlit Cloud部署

1. 将代码推送到GitHub仓库
2. 在 [Streamlit Cloud](https://streamlit.io/cloud) 创建新应用
3. 连接您的GitHub仓库
4. 设置主文件为 `main.py`
5. 部署完成后即可使用

## 使用说明

1. 在侧边栏输入您的OpenAI API密钥
2. 在聊天框中输入您的问题
3. 等待AI回复
4. 可以点击"重新开始会话"按钮清空对话历史

## 注意事项

- 需要有效的OpenAI API密钥
- 确保网络连接正常
- API调用可能产生费用

## 技术栈

- Streamlit - Web应用框架
- LangChain - LLM应用开发框架
- OpenAI API - 语言模型服务 