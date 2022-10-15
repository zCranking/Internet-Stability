import speedtest
import matplotlib.pyplot as plt
import time

downloadSpeed = []
uploadSpeed = []

for x in range(5):
    st = speedtest.Speedtest(secure=1)
    ds = round(st.download()/1000000, 2)
    downloadSpeed.append(ds)
    us = round(st.upload()/1000000, 2)
    uploadSpeed.append(us)
    time.sleep(10)
    print(downloadSpeed)
    print(uploadSpeed)
    
xaxes = (1, 2, 3, 4, 5)
plt.plot(xaxes, downloadSpeed, label="Download Speed")
plt.plot(xaxes, uploadSpeed, label="Upload Speed")
plt.title("Internet Speeds")
plt.legend()
plt.show()
         