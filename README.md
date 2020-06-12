# googleapi
Working with Google Geocoading API behind firewall

Install google geocoading api behind firewall

Enviornment Anaconda - Jupyter
set https_proxy=http://userid:password@proxy_IP:Proxy_Port

Note: I am having @ in my password so replaced @ with %40

Now in Jupyter Notebook 

import os

os.environ['http_proxy'] = "http://userid:password@proxy_IP:Proxy_Port" 

os.environ['https_proxy'] = "https://userid:password@proxy_IP:Proxy_Port"
