"""压测
"""
import json

from locust import HttpLocust, TaskSet, task


class HttpTest(TaskSet):

    def on_start(self):
        """初始化工作（登录、注册等）
        """
        pass

    @task(1)
    def hobby_detail(self):
        data = json.dumps(self.locust.hobby_detail_data)

        resp = self.client.post("/api/v1/hobby/detail",
                                data=data,
                                headers=self.locust.headers)
        content = json.loads(resp.text, encoding="utf-8")
        print("content:", content)

    # @task(1)  # task参数表示执行权重，值越大，执行概率越高
    # def hobby_list(self):
    #     self.client.post("/api/v1/hobby/list")


class HttpUser(HttpLocust):

    # locust -f test.py --host=http://192/168/0/102:8001 --port=8090

    # 待请求地址，也可以在命令行中使用--host参数指定
    host = "http://192.168.0.102:8002"

    # 指定TaskSet类
    task_set = HttpTest

    # 请求头
    headers = {"Content-Type": "application/json"}

    # 请求参数
    hobby_detail_data = {
        "hobbyId": 57
    }

    # 每个用户执行两个任务的时间间隔(单位: 毫秒)，
    # 上下限，具体值随机取，默认间隔位固定值1s
    min_wait = 1000
    max_wait = 3000
