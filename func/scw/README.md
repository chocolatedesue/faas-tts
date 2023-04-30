# 不要尝试直接放弃
线上alpine镜像 无法运行numpy 
可能办法: dockerfile从源码构建numpy 




## 注意事项
1. 目录执行问题。。尽量直接放在根目录下 导入包会有神奇问题
2. numpy  alpine Error loading shared library ld-linux-x86-64.so.2 No such file or directory 



auth:
https://www.scaleway.com/en/docs/compute/instances/api-cli/creating-managing-instances-with-cliv2/

https://www.scaleway.com/en/docs/serverless/functions/reference-content/functions-limitations/

依赖的文件夹只能是package/
https://github.com/scaleway/serverless-examples/tree/main/functions/python-dependencies


https://www.scaleway.com/en/docs/serverless/functions/reference-content/deploy-function/

