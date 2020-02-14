import random
from locust import HttpLocust, TaskSequence, seq_task, task
import json


class Benchmark(TaskSequence):
    def on_start(self):
        tokens = []
        with open('token.txt', 'r') as lines:
            tokens = [line.strip() for line in lines if len(line.strip()) > 20]
        self.tokens = tokens

    @seq_task(1)
    def task1(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(2)
    def task2(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=56&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(3)
    def task3(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=57&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(4)
    def task4(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=58&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(5)
    def task5(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=59&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(6)
    def task6(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114482&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(7)
    def task7(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114574&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(8)
    def task8(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114573&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(9)
    def task9(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114561&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(10)
    def task10(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=113975&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(11)
    def task11(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114568&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(12)
    def task12(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114570&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(13)
    def task13(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114566&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(14)
    def task14(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114482&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(15)
    def task15(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114533&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(16)
    def task16(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=114563&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(17)
    def task17(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/VOD/2/detail/100069772', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(18)
    def task18(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/related_detail_like/2/100069772?chapter_id=0&index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(19)
    def task19(self):
        token = random.choice(self.tokens).strip()
        with self.client.request('GET', 'content/v2.4/vi/related_detail_video/2/100069772?index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @seq_task(20)
    def task20(self):
        token = random.choice(self.tokens).strip()
        data = json.dumps({
            'baseURL': 'https://bkm.fbox.fpt.vn/bpk-vod/vod-nondrm/default/JordskottSeason1_2015_SE_01/JordskottSeason1_2015_SE_01/manifest.mpd',
            'menu_id': 2,
            'item_id': 100069772,
            'type': 0,
            'chapter_id': 320620,
            'is_trailer': 0
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


class Run(HttpLocust):
    task_set = Benchmark
