# 资产管理网站
该项目参考于网上的开源项目，为简单的资产管理网站，主要包含三块：
1.资产管理；2.人员管理；3.日志记录 
支持csv文件导出功能
我修改了原项目中冗余的数据库表结构，修改了一些views中的后台逻辑，项目中有一些有意思的写法，值得研究一下。
#技术栈：
后端采用python3.6 + django2.2  
前端采用html + css + js  

# 启动项目
1. 创建数据库，create database zcgl;  
2. 修改settings中的数据库配置，我改用了更轻量化的sqlite
3. 安装相关包，pip install -r requirements.txt
4. 迁移数据库，python manage.py migrate  
5. 创建超级用户，python manage.py createsuperuser  
6. 启动项目，python manage.py runserver

