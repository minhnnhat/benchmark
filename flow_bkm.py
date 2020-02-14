import random
from locust import HttpLocust, TaskSequence, seq_task, task, TaskSet
import json

tokens = None


class Benchmark(TaskSet):
  #  def on_start(self):
  #      if len(tokens) > 0:
  #          self.token = random.choice(tokens)
    # region EVENT
    @task
    def task1(self):
        with self.client.request('GET', '/bpk-tv/HTV7HD/default/HTV7HD.isml/index.m3u8', headers={'User-Agent':'Locust'}, catch_response=True, timeout=1) as response:
            if response.status_code == 200:
                response.success('OK')


class Run(HttpLocust):
    min_wait = 100
    max_wait = 100
    task_set = Benchmark

  #  def __init__(self):
  #      super(Run, self).__init__()
  #      global tokens
  #      if tokens is None:
  #          with open('token.txt', 'r') as lines:
  #              tokens = [line.strip()
  #                        for line in lines if len(line.strip()) > 20]
