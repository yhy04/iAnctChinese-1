from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "THUDM/glm-4"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 输入文本
text = "张三在北京大学读书。"
prompt = f"任务：从以下文本中提取实体，并按类别分类。\n文本：{text}\n输出："

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=128)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("NER 结果：", result)
