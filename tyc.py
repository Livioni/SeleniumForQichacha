from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import xlwt #excel文件写入
import xlrd #excel文件读取
from xlutils.copy import copy #excel文件复制
import random
from time import sleep

class web_browser(object):
    def __init__(self,company_name=0,address=0,credit_code=0,legal_person=0,\
                        registered_capital=0,status=0,type=0,business_num=0,business_term=0,\
                        introduction = 0, canbaorenshu = 0):
        option = webdriver.ChromeOptions()
        server = Service(executable_path='/Users/livion/Documents/GitHub/Sources/SeleniumForQichacha/chromedriver_m1')
        #初始化webbrowser实例
        self.driver = webdriver.Chrome(service = server,options=option)
        self.company_name,self.address,self.credit_code,self.legal_person,self.registered_capital,self.status,self.type,self.business_num,self.business_term,self.introduction,self.canbaorenshu = company_name,address,credit_code,legal_person,registered_capital,status,type,business_num,business_term,introduction,canbaorenshu
        ##维护列表：
        self.first_item_in_search_list_xpath = ['//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div[1]/a',\
                                                '//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/a',\
                                                '//*[@id="page-container"]/div/div[2]/section/main/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a',\
                                                '//*[@id="page-container"]/div/div[2]/section/main/div[3]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/a']
        self.credit_code_path ='//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/div/span[1]'
        self.name_xpath = '//*[@id="page-root"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h1'
        self.address_xpath = '//*[@id="page-root"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[4]/div[3]/div[2]/span[2]'     
        self.legal_person_xpath = '//*[@id="page-root"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div/span[2]/a[1]'
        self.registered_capital_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div'
        self.status_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]'
        self.type_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]'
        self.business_num_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/div/span[1]'
        self.business_term_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/span'
        self.introdunction_xpath = '//*[@id="page-root"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/div[4]/div[4]/div/div/div/span[2]'
        self.canbaorenshu_xpath = '//*[@id="page-root"]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[7]/td[6]'
        self.search_xpath = '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/div[1]/input'        
        self.re_search_xpath = '//*[@id="page-header"]/div/div[2]/div/div/div[1]/input'
        self.search_button_xpath = '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/button'
        self.search_click_button_xpath = '//*[@id="page-header"]/div/div[2]/div/div/button'
        self.clear_button_xpath = '//*[@id="page-header"]/div/div[2]/div/div/div/span'
        self.login_xpath = '//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div/div[6]/span'
        self.driver.get('https://www.tianyancha.com/')
        sleep(3)
        
    def login(self):
        #登陆
        self.driver.find_element(By.XPATH,self.login_xpath).click()
        sleep(10)
    
    def search(self,keyword):
        #向搜索框注入文字
        self.driver.find_element(By.XPATH,self.search_xpath).send_keys(keyword)
        #单击搜索按钮
        srh_btn = self.driver.find_element(By.XPATH,self.search_button_xpath)
        srh_btn.click()

    def re_search(self,keyword):
        #清除搜索框内容
        self.driver.find_element(By.XPATH,self.clear_button_xpath).click()
        # 向搜索框注入下一个公司地址
        self.driver.find_element(By.XPATH,self.re_search_xpath).send_keys(keyword)
        #搜索按钮
        srh_btn = self.driver.find_element(By.XPATH,self.search_click_button_xpath)
        srh_btn.click()
    
    def get_deeper(self):
        j = 0
        while True:
            try:                                               
                inner = self.driver.find_element(By.XPATH,self.first_item_in_search_list_xpath[j]).get_attribute("href")   
                break
            except:
                j += 1
                if j > len(self.first_item_in_search_list_xpath):
                    raise Exception('搜索列表第一企业名称的xpath路径未包含在列表中')
                continue
        self.driver.get(inner)
        sleep(1)


    def fetch_data(self):
        return_dic = {}
        sleep(1)
        if self.company_name:
            try:
                name = self.driver.find_element(By.XPATH,self.name_xpath).text
            except:
                name ='没有找到企业名称'  
            return_dic['企业名称'] = name
        
        if self.address:
            try:
                address = self.driver.find_element(By.XPATH,self.address_xpath).text
            except:
                address ='没有找到企业地址'  
            return_dic['企业地址'] = address

        if self.credit_code:
            try:
                credit_code = self.driver.find_element(By.XPATH,self.credit_code_path).text
            except:
                credit_code ='没有找到企业信用代码'  
            return_dic['信用代码'] = credit_code
        
        if self.legal_person:
            try:
                legal_person = self.driver.find_element(By.XPATH,self.legal_person_xpath).text
            except:
                legal_person ='没有找到企业法人'  
            return_dic['法人'] = legal_person

        if self.registered_capital:
            try:
                registered_capital = self.driver.find_element(By.XPATH,self.registered_capital_xpath).text
            except:
                registered_capital ='没有找到企业注册资本'  
            return_dic['注册资本'] = registered_capital
        
        if self.status:
            try:
                status = self.driver.find_element(By.XPATH,self.status_xpath).text
            except:
                status ='没有找到企业状态'  
            return_dic['企业状态'] = status

        if self.type:
            try:
                type = self.driver.find_element(By.XPATH,self.type_xpath).text
            except:
                type ='没有找到企业类型'  
            return_dic['企业类型'] = type

        if self.business_num:
            try:
                business_num = self.driver.find_element(By.XPATH,self.business_num_xpath).text
            except:
                business_num ='没有找到工商注册号'  
            return_dic['工商注册号'] = business_num

        if self.business_term:
            try:
                business_term = self.driver.find_element(By.XPATH,self.business_term_xpath).text
            except:
                business_term ='没有找到工商登记期限'  
            return_dic['工商登记期限'] = business_term

        if self.introduction:
            try:
                introduction = self.driver.find_element(By.XPATH,self.introdunction_xpath).text
            except:
                introduction ='没有找到企业简介'  
            return_dic['简介'] = introduction

        if self.canbaorenshu:
            try:
                renshu = self.driver.find_element(By.XPATH,self.canbaorenshu_xpath).text
            except:
                renshu ='没有参保人数'
            return_dic['参保人数'] = renshu 

        return return_dic
        

def read_excel(file_name,sheet_name,row_num = 1,column_num = 0):
    '''
    读取excel文件中的数据
    :param file_name: 文件名
    :param sheet_name: sheet名
    :para row_num: 起始行数（从0开始）
    :param column_num: 起始列数（从0开始）
    :return: sheet_copy 复制的表
    :return: inc_list 读取的数据(list)
    '''
    #从excel获取查询单位
    worksheet = xlrd.open_workbook(u'%s'%file_name)
    sheet1 = worksheet.sheet_by_name('%s'%sheet_name)
    rows = sheet1.nrows # 获取行数
    inc_list = []
    for i in range(row_num,rows) :
        data = sheet1.cell_value(i, column_num) # 取第1列数
        inc_list.append(data)
    print(inc_list)
    #写回数据
    writesheet1 = copy(worksheet)# 这里复制了一个excel，没有直接写回最初的文件。
    sheet_copy = writesheet1.get_sheet(0)
    return writesheet1, sheet_copy, inc_list


if __name__ == "__main__":
    newsheet,sheet_copy,company_list = read_excel('company.xls','Sheet1')
    d = web_browser(company_name=1,address=1,credit_code=1,legal_person=1,\
                        registered_capital=1,status=1,type=1,business_num=1,business_term=1,\
                        introduction=1,canbaorenshu=1)
    for i in range(0,len(company_list)):
        if i % 20 == 0:
            sleep(random.randint(5,15))
        company_txt = company_list[i]
        if i==0:
            # d.login()
            d.search(company_txt)
        else:
            d.re_search(company_txt)
        sleep(random.randint(2,3))
        d.get_deeper()
        info = d.fetch_data()
        if i==0:
            k = 0
            for key in info:
                sheet_copy.write(i,k+1,key)
                k += 1
        j = 0
        for key,value in info.items():
            sheet_copy.write(i+1,j+1,info[key])
            newsheet.save(u'finished.xls')
            j += 1
        
        print(company_txt,info)
    
    newsheet.save(u'finished.xls')
    d.driver.quit()



