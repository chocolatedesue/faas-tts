## 简介
利用各种faas部署dl模型或g2p服务

## faas研究结果
1. azure 可以简单有轮子  g2p和model都行 
2. aws lambda docker体验好 但是pricing不好  zip解压后250m限制 不能部署大模型和g2p
3. scaleway function alpine 对numpy不友好 pass


## 建议
1. container >> function 建议用基于container的serverless