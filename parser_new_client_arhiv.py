import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import password
import json
#https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_removed%5D=2&sort=-last_attend_date
class Selenium_test():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            executable_path=password.path_sel,
            options=options
        )
       
    def start(self,last_date_day_month, now_date_day_month, arhiv):
        self.driver.get('https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_removed%5D=2&sort=-first_payment_date&page=1&pageSize=500')
        time.sleep(1)
        email_input = self.driver.find_element(by=By.ID, value="loginform-username")
        email_input.clear()
        email_input.send_keys(password.login_alfa_samat)
        time.sleep(0.2)
        password_input = self.driver.find_element(by=By.ID, value="loginform-password")
        password_input.clear()
        password_input.send_keys(password.passowrd_alfa_samat)
        time.sleep(0.2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(1) 
        self.client_lesson(name_columns =[], last_date_day_month = last_date_day_month, now_date_day_month = now_date_day_month, arhiv = arhiv)
        
        
        

   

    def client_lesson(self,name_columns = ['ФИО'], last_date_day_month = '01.01', now_date_day_month = '01.01', arhiv = False):
        # with open(f'info_clients/json/{last_date_day_month}_info_client.json', encoding='utf-8') as f:
        # with open(f'info_clients/json/10.07_fits_lesson_sucses_arhiv_2_copy.json', encoding='utf-8') as f:
                    
        #     all_info_json = json.load(f)
       
        
        # count_student_in_arhiv = int(self.driver.find_element(By.XPATH, value = '//*[@id="w1"]/div[1]/span/b[2]').text)
        all_info_json = {}
        id_students = []
        for name_student in all_info_json.keys():
            id_students.append(all_info_json[name_student]['ID']) 
        print(len(all_info_json.keys()))
        print(1)
        input('Настройте столбики и нажмите Enter')
        #print(1)

        student_id_and_name=all_info_json
        head_colums = self.driver.find_element(By.TAG_NAME, 'thead')
        names_colums_client = head_colums.find_elements(By.TAG_NAME, 'th')
        columns = []
        for name_colum in names_colums_client:
            columns.append(name_colum.text)
        #print(columns)
        
        count = int(self.driver.find_element(By.XPATH,'//*[@id="w1"]/div[1]/span/b[2]').text)
        if count%500==0:
            count = count//500
        else:
            count = count//500
            count+=1
        
        for number_list_client in range(1,count+1):
            time.sleep(10)
            print(len(all_info_json.keys()))
            students_count = self.driver.find_element(By.TAG_NAME, 'tbody')
            students = students_count.find_elements(by=By.TAG_NAME, value = "tr")

            for number_student in range(len(students)):
                print(number_student)

                student = students[number_student].find_elements(by=By.TAG_NAME, value = "td")
                info_student = {}

                name_index = columns.index('ФИО') 
                id_index = columns.index('ID')
                date_k_index = columns.index('Дата конверсии')

                date_day_last = int(last_date_day_month.split('.')[0])
                date_month_last = int(last_date_day_month.split('.')[1])

                # if len(all_info_json.keys()) >= count_student_in_arhiv:
                #     with open(f'info_clients/json/{now_date_day_month}_new_info_client_arhiv.json', 'w', encoding='utf-8') as f:
                #         json.dump(student_id_and_name, f, ensure_ascii=False, indent=4)
                #     print('stop')
                #     exit()

                if student[id_index].text not in id_students:
                    id_students.append(student[id_index].text)
                    for name_column in columns:
                        if name_column!='' and name_column!=' ':
                            info_student[name_column] = student[columns.index(name_column)].text

                    student_id_and_name[student[name_index].text] = info_student
                # for name_column in columns:
                #     if name_column!='' and name_column!=' ':
                #         info_student[name_column] = student[columns.index(name_column)].text

                    student_id_and_name[student[name_index].text] = info_student
            
            if number_list_client != count:
                self.driver.get(f'https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_removed%5D=2&sort=-first_payment_date&page={number_list_client+1}&pageSize=500')

            else:
                with open(f'info_clients/json/{now_date_day_month}_info_client_arhiv.json', 'w', encoding='utf-8') as f:
                    json.dump(student_id_and_name, f, ensure_ascii=False, indent=4)
                print('stop')
    
        with open(f'info_clients/json/{now_date_day_month}_info_client_arhiv.json', 'w', encoding='utf-8') as f:
            json.dump(student_id_and_name, f, ensure_ascii=False, indent=4)
        print('stop')


    def dowland_list_start(self):
        try:
            return self.driver.find_element(By.XPATH, '//*[@id="w1-container"]/table/tbody/tr[1]/td[2]/a').text
        except:
            return self.dowland_list_start()
   
       

def start():
    arhiv = False
    last_date_day_month = '30.06'
    now_date_day_month = '08.08' 
    Selenium_test().start(last_date_day_month, now_date_day_month, arhiv)


start() 