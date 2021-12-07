from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# константы для selenium
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://dev1.redbridge-arm.com/#"
driver.get(url)
time.sleep(3)


# Эта функция авторизуется в системе
def start_work_red_bridge():
    # регестрация на сайте redbridge
    Login = driver.find_element_by_id("loginform-username")
    Login.send_keys("Admin_GP")
    Password = driver.find_element_by_xpath("//input[@class='form-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
    Password.send_keys("123456")
    sign_up = driver.find_element_by_tag_name("button").click()
    time.sleep(3)
    # Обновление страницы. Ибо сайт не способен загрузить нужную мне информацию, с первого раза!!!
    driver.refresh()
    print("вход в систему - успешно")


def go_to_client():
    link_to_clients = driver.find_elements_by_xpath("//a[@class='mat-list-item mat-focus-indicator ng-star-inserted']")[10]
    link_to_clients.click()
    link_to_clients = driver.find_elements_by_xpath("//a[@class='mat-list-item mat-focus-indicator ng-star-inserted']")[11]
    link_to_clients.click()
    print("Открытие клиентов - успешно")


def create_client():
    # Создаю нового клиента
    create_btn = driver.find_elements_by_xpath("//span[@class='ng-scope']")[1]
    create_btn.click()
    name_input = driver.find_element_by_xpath("//input[@placeholder='Название компании']")
    name_input.send_keys("Агропром")
    choose_3rd_line = driver.find_elements_by_xpath("//span[@class='select2-arrow ui-select-toggle']")[1]
    choose_3rd_line.click()
    choose_in_3rd_line = driver.find_element_by_xpath("//span[@class='level_0']").click()
    button_create = driver.find_element_by_xpath("//button[@class='btn btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    time.sleep(2)
    print("Создать клиента - успешно")


def work_with_about_client():
    website = driver.find_element_by_xpath("//input[@ng-model='$ctrl.company.site']")
    website.send_keys("www.agroprom.ru")
    email = driver.find_element_by_xpath("//input[@ng-model='$ctrl.company.email']")
    email.send_keys("agroprom@gmail.com")
    phone = driver.find_element_by_xpath("//input[@ng-model='$ctrl.company.landline_mask']")
    phone.send_keys("79854147825")
    tags = driver.find_element_by_xpath('//input[@ng-model="$select.search"]')
    tags.send_keys("Название тэга")
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']")
    save_btn.click()
    # Спроси про Холдинговые связи
    go_to_holding_relationships = driver.find_element_by_xpath("//a[text()='Холдинговые связи']").click()
    go_to_information = driver.find_element_by_xpath("//a[text()='Информация']").click()
    time.sleep(2)
    info_input = driver.find_element_by_xpath('//textarea[@ng-model="$ctrl.company.description"]')
    info_input.send_keys("Информация про компанию")
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']").click()
    go_to_manager = driver.find_element_by_xpath("//a[text()='Ответственный']").click()
    time.sleep(1)
    create_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    time.sleep(1)
    choose_btn = driver.find_elements_by_xpath("//span[@class='select2-arrow ui-select-toggle']")[0]
    choose_btn.click()
    manager_choose = driver.find_element_by_xpath("//div[text()='Ардаков Игорь Герасимович, Менеджер по продажам филиал Самара']").click()
    choose_btn = driver.find_elements_by_xpath("//span[@class='select2-arrow ui-select-toggle']")[1]
    choose_btn.click()
    potancial = driver.find_element_by_xpath("//div[@class='select2-result-label ui-select-choices-row-inner']//span").click()
    create_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']").click()
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']").click()
    print("О компании - успешно")


def work_with_contacts():
    go_to_contacts = driver.find_element_by_xpath("//a[text()='Контакты']").click()
    create_contact = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']").click()
    name_input = driver.find_element_by_xpath('//input[@ng-model="$ctrl.model.fullname"]')
    name_input.send_keys("Петров Александр Борисович")
    create_contact_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']").click()
    print("Контакты - успешно")


def work_with_address():
    go_to_address = driver.find_element_by_xpath("//a[text()='Адреса']").click()
    driver.refresh()
    time.sleep(7)
    address_input = driver.find_element_by_xpath('//input[@ng-model="$ctrl.ngModel"]')
    time.sleep(2)
    address_input.send_keys("Россия, Самара")
    time.sleep(2)
    choose_address = driver.find_element_by_xpath('//a[@ng-bind-html="match.label | uibTypeaheadHighlight:query"]').click()
    time.sleep(2)
    save_btn = driver.find_element_by_xpath("//a[@class='btn btn-primary btn-sm']").click()
    print("Адрес - успешно")


def work_with_potential():
    go_to_potential = driver.find_element_by_xpath("//a[text()='Потенциалы']").click()
    time.sleep(2)
    input_btn = driver.find_element_by_xpath("//button[@class='btn-xs btn btn-act-default ng-isolate-scope btn-success']").click()
    time.sleep(2)
    potential_input = driver.find_element_by_xpath('//input[@ng-model="$ctrl.potentialValue"]')
    potential_input.clear()
    potential_input.send_keys("10000000")
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']").click()
    print("Потенциалы - успешно")
    time.sleep(5)


def work_with_communication():
    go_to_communication = driver.find_element_by_xpath("//a[text()='Коммуникация']").click()
    time.sleep(2)
    create_action = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    time.sleep(2)
    # Сохраняем событие
    save_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-success btn-act']").click()
    time.sleep(2)
    close_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary dropdown-toggle"]').click()
    end_event_btn = driver.find_element_by_xpath("//a[text()='Завершить']").click()
    time.sleep(2)
    comment = driver.find_element_by_xpath("//textarea[@ng-model='$ctrl.comment.note']")
    comment.send_keys("Встреча прошла успешно")
    like_button = driver.find_element_by_xpath("//a[@class='btn btn-default']").click()
    end_comment = driver.find_element_by_xpath("//button[@id='simple-btn-keyboard-nav']").click()
    time.sleep(2)
    end_comment = driver.find_element_by_xpath("//a[text()='Завершить']").click()
    print("Событие - успешно")


def work_with_park():
    open_buttons = driver.find_element_by_xpath("//a[@class='rba-tab-label-content dropdown-toggle']").click()
    time.sleep(2)
    go_to_park = driver.find_element_by_xpath("//a[text()='Парк техники']").click()
    time.sleep(2)
    create_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']").click()
    time.sleep(2)
    next_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']").click()
    choose_tech = driver.find_element_by_xpath("//b[text()='Телескопический погрузчик JCB 540-140 HI-VIZ']").click()
    next_btn = driver.find_elements_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']")[1]
    next_btn.click()
    make_number = driver.find_element_by_xpath("//button[text()='Сгенерировать']").click()
    year_input = driver.find_element_by_xpath("//input[@format='YYYY']")
    year_input.send_keys("2021")
    # year_input.submit()
    data_sale = driver.find_element_by_xpath("//input[@format='DD.MM.YYYY']")
    data_sale.send_keys("08072021")
    # data_sale.submit()
    create_btn = driver.find_elements_by_xpath("//button[@class='btn btn-act-default ng-scope ng-isolate-scope btn-primary btn-act']")[1]
    create_btn.click()
    print("Товар - добавлен")


def work_with_counterparty():
    open_buttons = driver.find_element_by_xpath("//a[@class='rba-tab-label-content dropdown-toggle']").click()
    time.sleep(2)
    go_to_park = driver.find_element_by_xpath("//a[text()='Контрагенты']").click()
    time.sleep(2)
    create_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    name_input = driver.find_element_by_xpath("//input[@ng-model='$ctrl.model.name']").send_keys("ООО Агропром")
    create_btn = driver.find_element_by_xpath("//button[@class='btn btn-act-default ng-isolate-scope btn-primary btn-act']").click()
    time.sleep(2)
    INN_input = driver.find_element_by_xpath("//input[@ng-model='$ctrl.entity.inn']").send_keys("4456788991")


start_work_red_bridge()
go_to_client()
create_client()
work_with_about_client()
# work_with_contacts()
# work_with_address()
# work_with_potential()
# work_with_communication()
# work_with_park()
work_with_counterparty()
print("тест прошёл успешно =)")