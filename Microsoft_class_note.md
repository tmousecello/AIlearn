# Microsoft 機器學習課程


### 分類
監督式學習技術的一種  
將模型定型以預測某項目屬於何種類別    
針對每個可能類別判斷機率，為0~1的一個值  

### 混淆矩陣
可視化工具  
特別用於監督學習  
可直觀的表現誤判狀況  

| \ | 0  | 1 |
|-----|--------|---|
| 0 | 2 | 1 |
| 1 | 1 | 2 |  

模型預測為 0，而實際標籤為 0 (確判為否)  
模型預測為 1，而實際標籤為 1 (確判為真)  
模型預測為 0，而實際標籤為 1 (誤判為否)  
模型預測為 1，而實際標籤為 0 (誤判為真)  

例如:預測貓狗
共有15隻

|\ |dog|cat|
|-----|--------|--|
|Dog|6|2|
|cat|4|3|

資料格通常會加上陰影，越高的值顏色越深  
可以協助估算模型效度:  
1.正確性:  
預測的值中，有多少是正確的?  
2.重新叫用:  
在所有確認為確定的案件中，模型能辨識幾件?  
3.精確度:  
模型預測為確定的案例中，實際確定有多少?  


