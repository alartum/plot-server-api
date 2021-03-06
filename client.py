import time
from plotserver_api import PlotServerAPI, Project
from config import Config

key = b'2gS8MlgPhs-jknxmKJi9wBasWYvXjE6lXjGCnWMobns='
api_url = Config.API_ADDRESS

api = PlotServerAPI("alartum", key, api_url, verbose=True)
project = Project("project1", api, fresh_start=True)

project.add_files(["sin", "cos"])
project.prepare_project()

import math
t = 0
while True:
    project.add_frame("sin", t, math.sin(t/20))
    project.add_frame("cos", t, math.cos(t/20))
    project.send_frames()
    time.sleep(2)
    t += 1