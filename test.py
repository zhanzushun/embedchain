import os

from embedchain import App
from embedchain.config import AppConfig,BaseLlmConfig
os.environ["OPENAI_API_KEY"] = "sk-"

def add_doc(id1, txt1):
    appConfig1 = AppConfig(log_level="DEBUG", id=id1)
    app1  = App(appConfig1)
    app1.add_local('text', txt1)
    print(f'app1.token={app1.count()}')


def query(doc_id_list):
    if (len(doc_id_list) == 1):
        where = {"app_id": doc_id_list[0]}
    else:
        cond_list = []
        for doc_id in doc_id_list:
            cond_list.append({"app_id": doc_id})
        where={"$or": cond_list}
    
    app2  = App(AppConfig(log_level="DEBUG"))
    response = app2.query("关于鲁迅", BaseLlmConfig(stream = True, number_documents=5),  dry_run=True, where=where)
    for chunk in response:
        print(chunk, end="", flush=True)
    print('--------')

add_doc('1', '鲁迅又叫周树人')
add_doc('2', 'ooo是鲁迅粉丝')
add_doc('1', '鲁迅是绍兴人')
add_doc('2', '鲁迅写的小说有呐喊')
query(['1'])