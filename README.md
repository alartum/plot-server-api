# plot-server-api
Python API for communication with plot-server.

# How to Use

1. Register a user on the PlotServer of your choice;
2. Get your API key;
3. Install dependencies:
```bash
$ pip3 install cryptography requests
```
4. Download this library:
  ```bash
  $ git clone https://github.com/alartum/plot-server-api.git
  ```
5. Integrate API into your application:
```python
from plot_api import PlotAPI, Project

# Set key and API address
key = b'5uSN9ojYpMiI7gQ5k5NWR6kYvenDX97CmxC5aaUGdH8='
api_url = "http://someadress"

# Initialize API manager
api = PlotAPI("alartum", key, api_url, verbose=True)
# And create new project with
project = Project("project1", api, fresh_start=True)

# Add tags for different data to be tracked 
project.add_files(["sin", "cos"])
# And inform the server 
project.prepare_project()

import math
t = 0
while True:
    # Add new data to the manager 
    project.add_frame("sin", t, math.sin(t**2/50))
    project.add_frame("cos", t, math.cos(t/20))
    # And send frames when done
    project.send_frames()
    time.sleep(2)
    t += 1
```
