# Nvidia Jetson
https://developer.nvidia.com/embedded/jetson-nano-developer-kit  
下載JetPack SDK  
我的版本:L4T 32.5.1  
JerPack:4.5
安裝etcher  
格式化SD卡  
把系統刷到SD卡裡  
把SD卡插進去，金屬部分朝上  
如果要退出卡按一下就好，不要用摳的  
接上電  
我DC頭沒法用，不知道是板子還是電供的問題  
改用USB供電  
開機後按我同意  
選語言跟鍵盤還有時區  
創建使用者  
打開終端機  
檢查可用容量:  
```free -m```
禁用ZRAM:  
    ```sudo systemctl disable nvzramconfig```
增加交換空間:  
    ```sudo fallocate -l 4G /mnt/4GB.swap```  
    ```sudo chmod 600 /mnt/4GB.swap```  
    ```sudo mkswap /mnt/4GB.swap```  
將其加到/etc/fstab中:  
    ```sudo vi /etc/fstab```
切到insert模式  
在文件最後輸入:  
    ```/mnt/4GB.swap swap swap defaults 0 0```
按esc退回一般模式，按:進入指令模式，輸入:wq(儲存並退出)  
重新啟動  
再次檢查可用容量:  
    ```free -m```

無線網卡有問題  
無法驅動  
https://forums.developer.nvidia.com/t/edimax-ew-78111un-v2-wifi-setup/165047  
上面有教學
```  
wget https://www.edimax.com/edimax/mw/cufiles/files/download/Driver_Utility/EW-7811Un_V2_Linux_Driver_1.0.0.3.zip  
unzip EW-7811Un_V2_Linux_Driver_1.0.0.3.zip   
cd EW-7811Un_V2_Linux_Driver_1.0.0.3/  
tar xvf rtl8188EUS_linux_v5.3.9_28540.20180627.tar.gz   
cd rtl8188EUS_linux_v5.3.9_28540.20180627/   
# The next line is important
export ARCH=arm64  
make  
sudo make install  
sudo reboot now  
```
好像長期連網會斷線或不穩  
建議用有線網路  

測試csi鏡頭  
https://developer.nvidia.com/embedded/learn/tutorials/first-picture-csi-usb-camera  
記得把蓋子拔掉  
然後鏡頭要轉，對焦  
    ```nvgstcapture-1.0```  
j儲存圖片，q退出  
拍照:  
    ```nvgstcapture-1.0 --automate --capture-auto```

### 遠程連接
用usb連接電腦和nano  
https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/courseware/b2e02e999d9247eb8e33e893ca052206/63a4dee75f2e4624afbc33bce7811a9b/?activate_block_id=block-v1%3ADLI%2BS-RX-02%2BV2%2Btype%40sequential%2Bblock%4063a4dee75f2e4624afbc33bce7811a9b  
打開cmd  
```ssh <username>@192.168.55.1```  
打yes  
輸密碼  
接著 `ls` 顯示檔案
`mkdir -p ~/nvdli-data`
再次`ls`
可以看到檔案成功創建  

### docker
```
sudo docker run --runtime nvidia -it --rm --network host \
    --volume ~/nvdli-data:/nvdli-nano/data \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    --device /dev/video0 \
    nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.6.1
```

```
echo "sudo docker run --runtime nvidia -it --rm --network host \
    --volume ~/nvdli-data:/nvdli-nano/data \
    --volume /tmp/argus_socket:/tmp/argus_socket \
    --device /dev/video0 \
    nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.6.1" > docker_dli_run.sh
```
後面tag 4.5、4.6都可以用
執行script  
```./docker_dli_run.sh  ```
執行jupyter  
網址:192.168.55.1:8888  
密碼:dlinano  












