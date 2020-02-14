from sanic import Blueprint, Sanic
from sanic.response import text
import os

app = Sanic(__name__)

@app.listener('before_server_start')
async def setup(app, loop):
        cmd = "locust --host=https://api-devgateway.fbox.fpt.vn/content/v2.4/vi/IPTV/channel --locustfile=demo.py --slave --master-host=118.69.166.181"
        os.system(cmd)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5200, workers=4)


