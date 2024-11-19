from zhipuai import ZhipuAI
import json
# 初始化 ZhipuAI 客户端，填写您的 API Key
client = ZhipuAI(api_key="24a463e3442c20746ae8574b5d6f86a7.DbjlsnN5MUX7RZUQ")

# 发送请求以提取命名实体
response = client.chat.completions.create(
    model="glm-4",  # 使用的模型名称，例如 glm-4-plus
   messages=[
    {"role": "user", "content": "请提取以下文本中的命名实体：张三去了北京大学并参观了天安门广场。"},
    {"role": "assistant", "content": "好的，请告诉我您需要的实体分类。"},
    {"role": "user", "content": "需要人名、地名和机构名。请按json格式输出：{'人名': [], '地名': [], '机构名': []}"}
]

)

raw_result = response.choices[0].message.content
print(raw_result)
start_index = raw_result.find("{")
end_index = raw_result.rfind("}")


json_content = raw_result[start_index:end_index + 1]  # 提取 JSON
parsed_result = json.loads(json_content)  # 转换为 Python 字典
# 输出结果
print(parsed_result)

