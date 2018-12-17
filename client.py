from config import Config
import requests
from cryptography.fernet import Fernet
import json

class PlotAPI():
    def __init__(self, username, key, api_url):
        self.username = username
        self.key = key 
        self.api_url = api_url
        self.encoder = Fernet(key)

    def upload(self, entry, data):
        joined = self.username + data
        raw   = self.encoder.encrypt(joined.encode('utf8'))
        body = {
            "user": self.username,
            "raw" : raw.decode('utf-8')
        }
        res = requests.post(self.api_url + entry, data=json.dumps(body))
        print(res.text)

class Project():
    def __init__(self, name, plot_api, fresh_start=False):
        self.name = name;
        self.fresh_start = fresh_start;
        self.cleaned = not fresh_start;
        self.plot_api = plot_api
        self.files = []
        self.frames = {}
        self.upload_entry = "/api/upload"

    def add_files(self, files):
        for file in files:
            self.files.append(file)

    def add_frame(self, file, step, value):
        if file not in self.files:
            print('Error: File {} is not detected in project {}.'.format(file, self.name)) 
        self.frames[file] = [step, value]

    def send_frames(self):
        mode = "/a"
        if not self.cleaned:
            mode = "/w"
            self.cleaned = True
        raw = json.dumps([self.name, self.frames])
        self.plot_api.upload(self.upload_entry+mode, raw)
        self.frames = {}

key = b'2gS8MlgPhs-jknxmKJi9wBasWYvXjE6lXjGCnWMobns='
api_url = Config.API_ADDRESS

api = PlotAPI("alartum", key, api_url)
project = Project("test", api, fresh_start=True)

project.add_files(["xs", "ys"])
for i in range(3):
    project.add_frame("xs", i, i**2)
    project.add_frame("ys", i, i**0.5)
    project.send_frames()