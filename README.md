# SeleiumForCAICT
 企查查之seleium自动化操作：该脚本可按照Excel已有企业名称数据在企查查上自动搜索企业地址，法人等信息。

  例如：需要查找重庆上市企业信息，已有企业名称，遂编写该脚本实现自动化操作。

## 依赖库

- selenium                   4.2.0

- xlrd                       2.0.1
- xlutils                    2.0.0
- xlwt                       1.3.0

## 使用说明

1. 在 https://chromedriver.chromium.org/home 下载对应版本的chromedriver，并修改qcc.py 16行中server路径为chromedriver路径。

2. 按照company.xls的格式输入要查询的企业名称。（可以模糊搜索，但结果取第一个）

3. 修改qcc.py 171行

   ```python
   d = web_browser(company_name=0,address=1,credit_code=1,legal_person=1,\
                       registered_capital=1,status=1,type=1,business_num=1,business_term=1,\
                           introduction = 0)
   ```

   在初始化实例参数中，对应参数=1表示搜索并记录该数据。

   company_name：企业名称

   address：地址

   credit_code：统一社会信用代码

   legal_person：法人

   registered_capital：注册资本

   status：企业状态

   type：企业类型

   business_num：工商注册号

   business_term：营业期限

   introduction：简介

4. run qcc.py

## 其他

运行之前需要手动扫码登陆企查查。

实际运行下来 55个企业需要7分钟的时间，实际还能更快。

该脚本在同一个IP查询几百次后会被企查查监测并*暂停*访问，需要重新运行脚本执行剩下未查的企业。

查询更多次后有时会*停止*访问，这时就需要连个热点了。。。。



![处理前](README.assets/%E6%88%AA%E5%B1%8F2022-07-13%2022.22.11.png)

![处理后](README.assets/%E6%88%AA%E5%B1%8F2022-07-13%2022.22.43.png)



