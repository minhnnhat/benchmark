from sanic import Blueprint, Sanic
from sanic.response import text
import os

#proxy = 'http://210.245.31.16:80'

#os.environ['http_proxy'] = proxy
#os.environ['HTTP_PROXY'] = proxy
#os.environ['https_proxy'] = proxy
#os.environ['HTTPS_PROXY'] = proxy 
app = Sanic(__name__)

@app.listener('before_server_start')
async def setup(app, loop):
	cmd = "./env3/bin/locust --host=https://apiv2-gateway.fbox.fpt.vn/ --locustfile=sequence_pro_1.py --slave --master-host=172.20.2.52"
	os.system(cmd)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5200, workers=4)

