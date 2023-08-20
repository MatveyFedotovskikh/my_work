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
       
    def start(self, now_date_day_month, arhiv):
        self.driver.get('https://rtschool.s20.online/company/1/customer/index?page=1&pageSize=20&sort=-first_payment_date')
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
        self.run_student_and_parser_info(name_columns =[], now_date_day_month = now_date_day_month, arhiv = arhiv)
        
        
        

   

    def run_student_and_parser_info(self,name_columns = ['ФИО'], now_date_day_month = '01.01', arhiv = False):
        global json_students
        # with open(f'info_clients/json/{now_date_day_month}_info_client.json', encoding='utf-8') as f:
        with open(f'info_clients/json/09.08_info_client_arhiv.json', encoding='utf-8') as f:
            json_students = json.load(f)

        

        id_students = []

        for name_student in json_students.keys():
            id_students.append(json_students[name_student]['ID']) 

        for student in json_students.keys():
            id_student = json_students[student]["ID"]
            json_students[student]["link_alfa_crm"] = f'https://rtschool.s20.online/company/1/customer/view?id={id_student}'
            if "plan" not in json_students[student].keys():
                self.driver.get(f'https://rtschool.s20.online/company/1/customer/view?id={id_student}')
                self.run_in_student_lessons(student)
        

        
        with open(f'info_clients/json/09.08_all_info_client_arhiv_2.0.json', 'w', encoding='utf-8') as f:
            json.dump(json_students, f, ensure_ascii=False, indent=4)

        print('stop')
    def run_in_student_lessons(self, student):
        global json_students
        
        # ion-person popover-container m-r-xxs - отменен 
        # bg-success text-navy done_paid pull-left m-b-xs m-r-xs text-center bob-field  -  был
        # bg-success text-navy planned_paid pull-left m-b-xs m-r-xs text-center bob-field  -  будет
        # bg-warning text-warning absence_free pull-left m-b-xs m-r-xs text-center bob-field  - бесплатный пропуск
        # bg-warning text-danger absence_paid pull-left m-b-xs m-r-xs text-center bob-field  -  пропуск оплачен
        # bg-success text-navy planned_paid bob-comment bob-alert pull-left m-b-xs m-r-xs text-center bob-field  -  проведен но не отмечен
        # gray-bg planned_unpaid bob-comment bob-alert pull-left m-b-xs m-r-xs text-center bob-field - забыли провести
        # bg-info done_free pull-left m-b-xs m-r-xs text-center bob-field  - бесплатный урок
        # bg-info done_free pull-left m-b-xs m-r-xs text-center bob-field  - бусплатный ПУ
                                                                     
        lessons_true = self.driver.find_elements(By.XPATH, '//div[@class="bg-success text-navy done_paid pull-left m-b-xs m-r-xs text-center bob-field"]')  # проведен зеленый
        lessons_free_missed = self.driver.find_elements(By.XPATH, '//div[@class="bg-warning text-warning absence_free pull-left m-b-xs m-r-xs text-center bob-field"]') # бесплатный пропуск
        lessons_paid_missed = self.driver.find_elements(By.XPATH, '//div[@class="bg-warning text-danger absence_paid pull-left m-b-xs m-r-xs text-center bob-field"]') # платный пропуск
        lessons_done_not_filled = self.driver.find_elements(By.XPATH, '//div[@class="bg-success text-navy planned_paid bob-comment bob-alert pull-left m-b-xs m-r-xs text-center bob-field"]') # проведен но не отмечен
        lessons_not_done = self.driver.find_elements(By.XPATH, '//div[@class="gray-bg planned_unpaid bob-comment bob-alert pull-left m-b-xs m-r-xs text-center bob-field"]') # забыли провести
        lesson_on_credit = self.driver.find_elements(By.CLASS_NAME, value="bg-danger") #  проведен или пропуск в долг
        lesson_done_free = self.driver.find_elements(By.CLASS_NAME, value="bg-info") #  Беслпатный урок был возможно ПУ
        lesson_canceled = self.driver.find_elements(By.CLASS_NAME, value='ion-person popover-container m-r-xxs') #  отменен
        
        count_lessons = len(lessons_true) + len(lessons_free_missed)+len(lessons_paid_missed)+len(lessons_done_not_filled) + len(lessons_not_done)+len(lesson_on_credit)+len(lesson_done_free) + len(lesson_canceled) - 3
        
        count_fact_lessons = int(str(self.driver.find_element(By.XPATH,f'//*[@id="lessons-container"]/a').text)[2:].split(' / ф ')[1])
        count_planned_lessons = int(str(self.driver.find_element(By.XPATH,f'//*[@id="lessons-container"]/a').text)[2:].split(' / ф ')[0])
        json_students[student]["plan"] = count_planned_lessons
        json_students[student]["fact"] = count_fact_lessons
        if "Дата первого урока" not in json_students[student].keys():
            json_students[student]["Дата первого урока"] = ''
        if json_students[student]["Дата первого урока"] == "":
        
            PY = False
            for lesson in range(1,count_lessons+2):
                
                # maybi_nuber=2
                # try:
                #     self.dowland_list_start()
                                                                        
                #     lesson_done = self.driver.find_element(By.XPATH,f'//*[@id="customer-pjax"]/div[2]/div[1]/div[1]/div/div/div[{maybi_nuber}]/div/form/div[2]/div[{lesson}]').get_attribute('class') 
                # except:
                #     maybi_nuber=3
                #     lesson_done = self.driver.find_element(By.XPATH,f'//*[@id="customer-pjax"]/div[2]/div[1]/div[1]/div/div/div[{maybi_nuber}]/div/form/div[2]/div[{lesson}]').get_attribute('class') 
                lesson_no_flag = self.dowland_list_start(lesson)                                                                 
                
                                                                                                                                                                        
                
                if count_fact_lessons==0: 
                    json_students[student]["Дата первого урока"] = 'Не было уроков даже ПУ'
                    break

                if count_fact_lessons > count_lessons: 
                    json_students[student]["Дата первого урока"] = 'Первый урок был больше года назад'
                    break
                
                if count_fact_lessons <= count_lessons:
                    PY = True
                
                
                

                                    
                if lesson_no_flag.find('pull-left m-r-xs m-b-xs text-center font-bold bob-divider') !=-1 :
                    json_students[student]["Дата первого урока"] = 'за последние 365 дней не было первых уроков'
                    break

                else:   
                    lesson_done = self.driver.find_element(By.XPATH, f'//*[@id="spongebob-container"]/div/div/form/div[2]/div[{lesson}]/i[1]').get_attribute('class') 
                    lesson_done_true = False
                    if lesson_done == 'fa fa-check bob-done':
                        lesson_done_true = True  
                                                                
                    # //*[@id="spongebob-container"]/div/div/form/div[2]/div[9]
                    lesson_no_PY = self.driver.find_element(By.XPATH,f'//*[@id="spongebob-container"]/div/div/form/div[2]/div[{lesson}]/i[2]').get_attribute('class')
                    if lesson_no_PY.find('ion-asterisk') != -1:
                        PY = True

                    elif lesson_done_true:

                        if PY:
                            json_students[student]['date_first_lesson'] = self.driver.find_element(By.XPATH,f'//*[@id="spongebob-container"]/div/div/form/div[2]/div[{lesson}]').get_attribute('data-date')
                            self.driver.find_element(By.XPATH,'//*[@id="customer-pjax"]/div[1]/div/div/a[2]/span').click()
                            self.dowland_list_option()
                            self.driver.find_element(By.XPATH,'//*[@id="perv_urok_160"]').clear()
                            date_first_lesson = json_students[student]['date_first_lesson'].split('-')
                            date = f'{date_first_lesson[2]}-{date_first_lesson[1]}-{date_first_lesson[0]}'
                            self.driver.find_element(By.XPATH,'//*[@id="perv_urok_160"]').send_keys(date)
                            self.driver.find_element(By.XPATH,'//*[@id="w0"]/div[3]/button[2]').click()
                            self.dowland_list_start(lesson)
                            break

                        self.driver.find_element(By.XPATH,f'//*[@id="spongebob-container"]/div/div/form/div[2]/div[{lesson}]').click()
                        id_box_lesson = self.dowland_window_lesson()
                        self.driver.find_element(By.XPATH,f'//*[@id="{id_box_lesson}"]/div[2]/div[2]/div[1]/a').click()
                                                                            
                        number_lesson = self.dowland_window_in_lesson()
                        self.dowland_window_in_lesson3()
                        self.dowland_list_start(lesson)

                        if number_lesson != '1' and number_lesson != 'Не задано':
                            json_students[student]["Дата первого урока"] = 'Первый урок был больше года назад'
                            break

                        elif number_lesson == 'Не задано':
                            json_students[student]["Дата первого урока"] = 'В уроке не задан номер урока'
                            break
                        
                        else:
                            json_students[student]["Дата первого урока"] = self.driver.find_element(By.XPATH,f'//*[@id="customer-pjax"]/div[2]/div[1]/div[1]/div/div/div[{maybi_nuber}]/div/form/div[2]/div[{lesson}]').get_attribute('data-date')
                            self.driver.find_element(By.XPATH,'//*[@id="customer-pjax"]/div[1]/div/div/a[2]/span').click()
                            self.dowland_list_option()
                            self.driver.find_element(By.XPATH,'//*[@id="perv_urok_160"]').clear()
                            date_first_lesson = json_students[student]["Дата первого урока"].split('-')
                            date = f'{date_first_lesson[2]}-{date_first_lesson[1]}-{date_first_lesson[0]}'
                            self.driver.find_element(By.XPATH,'//*[@id="perv_urok_160"]').send_keys(date)
                            self.driver.find_element(By.XPATH,'//*[@id="w0"]/div[3]/button[2]').click()
                            self.dowland_list_start(lesson)

                            break

    def dowland_list_start(self,lesson):
        try:
            return self.driver.find_element(By.XPATH, f'//*[@id="spongebob-container"]/div/div/form/div[2]/div[{lesson}]').get_attribute('class')
        except:
            return self.dowland_list_start(lesson)
        
    def dowland_list_option(self):
        try:
            return self.driver.find_element(By.XPATH, f'//*[@id="customer-name"]')
        except:
            self.dowland_list_option()
    
    def dowland_window_lesson(self):
        try:
            return self.driver.find_element(By.CLASS_NAME,'popover').get_attribute('id')
        except:
            return self.dowland_window_lesson()
        
    def dowland_window_in_lesson(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="nomer_104_chosen"]/a').text
        except:
            return self.dowland_window_in_lesson()
        
    def dowland_window_in_lesson2(self):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@id="common-modal"]/div/div/div/button/span').click()
                    
        except:
            return self.dowland_window_in_lesson3()
        
    def dowland_window_in_lesson3(self):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@id="common-modal-lg"]/div/div/div/button/span').click()
        except:
            return self.dowland_window_in_lesson2()
        
def start():
    arhiv = False
    now_date_day_month = '08.08' 
    Selenium_test().start(now_date_day_month, arhiv)


start() 