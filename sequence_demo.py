import random
from locust import HttpLocust, TaskSequence, seq_task, task


class Benchmark(TaskSequence):
    def on_start(self):
        tokens = []
        with open('token_dev.txt', 'r') as lines:
            tokens = [line.strip() for line in lines if len(line.strip()) > 20]
        self.tokens = tokens

    @seq_task(1)
    def task1(self):
        token = random.choice(self.tokens).strip()
        self.client.request('GET', 'content/v2.4/vi/Home/list_section',
                            headers={'authorization': 'Bearer %s' % (token)}, timeout=3)

    @seq_task(2)
    def task2(self):
        token = random.choice(self.tokens).strip()
        self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=56&index=0&page_size=30&is_topic=false',
                            headers={'authorization': 'Bearer %s' % (token)}, timeout=3)

    @seq_task(3)
    def task3(self):
        token = random.choice(self.tokens).strip()
        self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=57&index=0&page_size=30&is_topic=false',
                            headers={'authorization': 'Bearer %s' % (token)}, timeout=3)

    @seq_task(4)
    def task4(self):
        token = random.choice(self.tokens).strip()
        self.client.request('GET', 'content/v2.4/vi/Home/section?section_id=58&index=0&page_size=30&is_topic=false',
                            headers={'authorization': 'Bearer %s' % (token)}, timeout=3)

    @seq_task(5)
    def task5(self):
        token = random.choice(self.tokens).strip()
        self.client.request('GET', 'content/v2.4/vi/IPTV/channel',
                            headers={'authorization': 'Bearer %s' % (token)}, timeout=3)


class Run(HttpLocust):
    task_set = Benchmark
