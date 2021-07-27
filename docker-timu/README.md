## 功能说明

用于启动timu二级目录下的Dockerfile或者docker-compose.yml服务

对于Dockerfile会自动build和run，自动累加端口号(见run.py的PORT_START定义)，默认已--rm模式启动

## 运行
python3 run.py

## 样例
题目格式见目录01-shili

## Tips
对于题目建议不设计可以修改和删除文件的权限。