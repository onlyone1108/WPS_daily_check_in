invite_userid = 244668941

import requests

sids = [
    "V02SSHKDEJYmVh0s-r21qNf2m34J1M400abdb5a80026bd5b05",
    "V02SH1_Z48musYp1w-YIm5bkP3K0tTM00ae6089b001641e113",
]

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
for i in sids:
    requests.post(invite_url, headers={'sid': i}, data={'invite_userid': invite_userid})
    
