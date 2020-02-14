import random
from locust import HttpLocust, TaskSequence, seq_task, task, TaskSet
import json

tokens = None


class Benchmark(TaskSet):
    def on_start(self):
        if len(tokens) > 0:
            self.token = random.choice(tokens)
    # region VOD
    @task
    def task1(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task2(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=56&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task3(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=57&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task4(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=58&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task5(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=59&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task6(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114482&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task7(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114574&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task8(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114573&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task9(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114561&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task10(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=113975&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task11(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114568&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task12(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114570&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task13(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114566&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task14(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114482&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task15(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114533&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task16(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=114563&index=0&page_size=30&is_topic=true', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task17(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/VOD/2/detail/100069772', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task18(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/related_detail_like/2/100069772?chapter_id=0&index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task19(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/related_detail_video/2/100069772?index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task110(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/check_follow/2/100069772', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task111(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/check_favorite/2/100069772', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task112(self):
        token = self.token
        data = json.dumps({
            "baseURL": "https://bkm.fbox.fpt.vn/bpk-vod/vod-nondrm/default/JordskottSeason1_2015_SE_01/JordskottSeason1_2015_SE_01/manifest.mpd",
            "menu_id": 2,
            "item_id": 100069772,
            "type": 0,
            "chapter_id": 320620,
            "is_trailer": 0
        })
        with self.client.request('POST', 'content/v2.6/vi/get_link', data=data, headers={'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))
    @task
    def task113(self):
        token = self.token
        with self.client.request('GET', 'account/v2.6/vi/Account/check_access', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))

   # endregion VOD

   # region IPTV
    @task
    def task21(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/IPTV/channel', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task22(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/IPTV/categories', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task23(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/IPTV/broadcast_schedule/1?day=10&month=9&year=2019', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task24(self):
        token = self.token
        data = json.dumps({
            "baseURL": "https://bkm.fbox.fpt.vn/bpk-vod/vod-nondrm/default/JordskottSeason1_2015_SE_01/JordskottSeason1_2015_SE_01/manifest.mpd",
            "menu_id": 2,
            "item_id": 100069772,
            "type": 0,
            "chapter_id": 320620,
            "is_trailer": 0
        })
        with self.client.request('POST', 'content/v2.6/vi/get_link', data=data, headers={'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task25(self):
        token = self.token
        with self.client.request('GET', 'account/v2.6/vi/Account/check_access', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))
   # endregion IPTV

   # region EVENT
    @task
    def task31(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task32(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=61&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task33(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=62&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task34(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Event/detail/8978', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task35(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/check_follow/2/100069772', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task36(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/related_detail_like/4/8978?chapter_id=8978&index=0&page_size=30&is_more=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task37(self):
        token = self.token
        data = json.dumps({
            "baseURL": "https://bkm.fbox.fpt.vn/bpk-vod/vod-nondrm/default/JordskottSeason1_2015_SE_01/JordskottSeason1_2015_SE_01/manifest.mpd",
            "menu_id": 2,
            "item_id": 100069772,
            "type": 0,
            "chapter_id": 320620,
            "is_trailer": 0
        })
        with self.client.request('POST', 'content/v2.6/vi/get_link', data=data, headers={'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task38(self):
        token = self.token
        with self.client.request('GET', 'account/v2.6/vi/Account/check_access', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))
   # endregion EVENT

   # region SPORT
    @task
    def task41(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/list_section', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task42(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Home/section?section_id=60&index=0&page_size=30&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task43(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/list_section/3', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task44(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/section/3?section_id=43&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task45(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/section/3?section_id=32&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task46(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/section/3?section_id=33&index=0&page_size=30&is_filter=false&is_more=false&is_topic=false', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
            if response.status_code == 200:
                r = response.json()
                if r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task47(self):
        token = self.token
        with self.client.request('GET', 'content/v2.6/vi/Sport/detail/38963', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True, timeout=3) as response:
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
        with self.client.request('POST', 'content/v2.6/vi/get_link', data=data, headers={'Authorization': 'Bearer %s' % (token), 'Content-Type': 'application/json'}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()
            elif response.status_code == 200:
                r = response.json()
                if r['result'] == 1:
                    response.success()
                elif r['result'] == 0:
                    response.failure(str(r['error']))

    @task
    def task49(self):
        token = self.token
        with self.client.request('GET', 'account/v2.6/vi/Account/check_access', headers={'authorization': 'Bearer %s' % (token)}, catch_response=True) as response:
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
    min_wait = 100
    max_wait = 100
    task_set = Benchmark

    def __init__(self):
        super(Run, self).__init__()
        global tokens
        if tokens is None:
            with open('token_dev.txt', 'r') as lines:
                tokens = [line.strip()
                          for line in lines if len(line.strip()) > 20]
