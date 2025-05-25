from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    try:
        model = ChatOpenAI(
            model="gpt-3.5-turbo", 
            openai_api_key=openai_api_key,
            base_url="https://api.aigc369.com/v1"  # 使用base_url替代openai_api_base
        )
        chain = ConversationChain(llm=model, memory=memory)
        
        response = chain.invoke({"input": prompt})
        return response["response"]
    except Exception as e:
        return f"抱歉，发生了错误：{str(e)}"

