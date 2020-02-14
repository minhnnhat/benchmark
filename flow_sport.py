import random
from locust import HttpLocust, TaskSequence, seq_task, task, TaskSet
import json

tokens = None


class Benchmark(TaskSet):
    def on_start(self):
        if len(tokens) > 0:
            self.token = random.choice(tokens)

    # region SPORT
    @task
    def task41(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task42(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=60&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task43(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/list_section/3', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task44(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/section/3?section_id=43&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task45(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/section/3?section_id=32&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task46(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/section/3?section_id=33&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task47(self):
        token = self.token
        with self.client.request('GET', 'content/v2.4/vi/Sport/detail/40170', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task48(self):
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

    # endregion SPORT


class Run(HttpLocust):
    # min_wait = 1000
    # max_wait = 3000
    task_set = Benchmark

    def __init__(self): 
        super(Run, self).__init__() 
        global tokens
        if tokens is None:
            with open('token.txt', 'r') as lines:
                tokens = [line.strip() for line in lines if len(line.strip()) > 20]