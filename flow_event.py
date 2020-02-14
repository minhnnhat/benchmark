import random
from locust import HttpLocust, TaskSequence, seq_task, task, TaskSet
import json

tokens = None


class Benchmark(TaskSet):
    def on_start(self):
        if len(tokens) > 0:
            self.token = random.choice(tokens)
    # region EVENT
    @task
    def task31(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task32(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=61&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task33(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=62&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task34(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Event/detail/8978', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task35(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/related_detail_like/4/8978?chapter_id=8978&index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task36(self):
        token = self.token
        data = json.dumps({
            "baseURL": "https://bkm.fbox.fpt.vn/bpk-vod/vod-nondrm/default/JordskottSeason1_2015_SE_01/JordskottSeason1_2015_SE_01/manifest.mpd",
            "menu_id": 2,
            "item_id": 100069772,
            "type": 0,
            "chapter_id": 320620,
            "is_trailer": 0
        })
        with self.client.request('POST', 'content/v2.4/vi/get_link', data=data, headers={'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))
    # endregion EVENT


class Run(HttpLocust):
    # min_wait = 1000
    # max_wait = 3000
    task_set = Benchmark

    def __init__(self):
        super(Run, self).__init__()
        global tokens
        if tokens is None:
            with open('token.txt', 'r') as lines:
                tokens = [line.strip()
                          for line in lines if len(line.strip()) > 20]
