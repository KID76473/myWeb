import json

array = [1, 2, 3, 4, 5]
json_array = json.dumps(array, indent=4)
print(json_array)

# llist = ["<Job AI Expert Engineer – Large Scale Model Engineer TCL Corporate Research(HK) Co., Ltd>", "<Job Deep Learning Software QA Engineer Intern NVIDIA>", "<Job Machine Learning Engineer Apple>", "<Job Machine Learning Engineer 恩士迅信息科技(上海)有限公司>", "<Job Machine Learning Engineer Graphcore>", "<Job Data Technical Engineer IBM>", "<Job Software Dev Engineer Intern, 2023 Beijing Amazon Business>", "<Job NLP Engineer 自然语言处理工程师 Evalueserve>", "<Job Lead Machine Learning Engineer - Trust Platform Grab>", "<Job 【WuTong Talent Program】Quant Developer UBIQUANT>", "<Job Machine Learning Engineer - New Grad 2023 空中云汇(深圳)网络科技有限公司>", "<Job Associate Software Engineer, gReach Program for People with Disabilities Google>"]
llist = {1: {1: 3, 2: 4}}
json_list = json.dumps(llist, indent=4)
print(json_list)
