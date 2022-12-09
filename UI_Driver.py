#!/usr/bin/env python
# -*- coding:utf-8 -*-

########################################################################
# Name: UI_Driver.py                                                   #
# Author:sunwei17                                                      #
# ver:0.1                                                              #
# Date:2022-12-09T15:10                                                #
########################################################################

import json
import time

from LoginWindow import *
from RD_GuideWindow import *
from MessageBox import *
from ConnectWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import base64

# 用requests准备实现不打开网页直接输账号密码，未实现
# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options

# sso的登录url
sso_url = "https://sso.hisense.com/login?"
# plm的登录url
plm_url = 'https://kdplm.hisense.com/enovia/emxLogin.jsp'

# 雷区搜索的url
leiQu_url = 'https://kdplm.hisense.com/enovia/common/emxTable.jsp?' \
            'sortColumnName=originated&SuiteDirectory=engineeringcentral&showPageHeader=' \
            'false&HelpMarker=emxhelpmyviewparts&program=HBMTMaterialAndProductJPO%3AfindMy' \
            'ViewObjects&type=type_HBMTMinefields&portalMode=true&subHeader=emxFramework.' \
            'String.LatestModifiedDocumentsByUser&StringResourceFileId=emxEngineeringCentral' \
            'StringResource&mode=Recent&toolbar=HBMTMineSearchToolbar&sortDirection=descending&' \
            'freezePane=Name%2CRouteStatus%2CTitle%2CActions%2CNewWindow&selection=multiple&portalCmdName=' \
            'HBMTMyMineList&jsTreeID=null&header=emxFramework.String.MyRecentDocuments&suiteKey=ProgramCentral' \
            '&clearLimitNotice=true&portal=ENCMyENGView&editLink=false&table=HBMTShowMineView&policy=policy_' \
            'HBMTSpecification'

rc_url = 'https://kdplm.hisense.com/enovia/common/emxTable.jsp?SuiteDirectory=' \
         'engineeringcentral&showPageHeader=false&hideHeader=true&pagination=100&HelpMarker=' \
         'emxhelpmyviewparts&program=HBMTPartsPriorityLibrary%3AgetHBMTParts&headerRepeat=0&type=' \
         'Part&FilterFrameSize=72&portalMode=true&StringResourceFileId=emxEngineeringCentralStringResource&' \
         'toolbar=HBMTPartPriorityToolbar&mode=view&sortDirection=descending&selection=multiple&portalCmdName=' \
         'HBMTPriorityLibraryParts&jsTreeID=null&suiteKey=Framework&header=emxEngineeringCentral.EngView.' \
         'MyView&portal=ENCMyENGView&editLink=false&FilterFramePage=..%2FsearchFilter%2FHBMTTableFilter' \
         'PriorityPart.jsp&table=HBMTPartPriorityLibrarySummaryTable'

# bom_url = 











class LoginWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = Ui_Login()
        self.main_ui.setupUi(self)
        self.defaultWindowFlag = self.windowFlags()  # 保存当前默认窗体设置
        
        
class ConnectWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.connect_ui = UiConnectWindow()
        self.connect_ui.setup_ui(self)
        self.lineEdit = None
        self.lineEdit_2 = None
        
        
class RD_GuideWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = Ui_MainWindow1()
        self.child.setupUi(self)
        self.defaultWindowFlag = self.windowFlags()  # 保存当前默认窗体设置
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(self.defaultWindowFlag | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) # 窗口置顶，无边框
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowTitleHint)  # 窗口置顶，显示标题栏
        self.window_locked = True  # 创建公共变量window_locked, 记录解锁按键的状态
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        
        
class MessageBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)
        
        
def open_leiQu_url():
    """
    # 这里用cookie确实可以实现不输入账号密码登录，但1:与输入账号密码登录一样，需要打开一次登录页面，2:打开雷区url显示的是plm首页，毫无意义
    # 如果把driver写在按钮事件里，每次按钮调用保存的cookie，都要重新打开一次登录页面
    driver = webdriver.Firefox()
    # driver.get(plm_url)
    # driver.get(sso_url)
    driver.get(leiQu_url)
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
    for cookie in cookies:
        cookie.pop('domain')
        driver.add_cookie(cookie)
    driver.get(leiQu_url)  # 第一次打开是PLM首页
    driver.get(leiQu_url)
  
    # 不用cookie，直接账号密码登录方案  
    # box_username = login.main_ui.lineEdit.text()
    # box_password = login.main_ui.lineEdit_2.text()
    # driver = webdriver.Firefox()
    driver.get(plm_url)
    # driver.get(leiQu_url)
    # username = driver.find_element(By.ID, 'login_name')
    # 如果实现在控制已打开的浏览器页面，则可以加个是否需要登录的判断
    # if driver.find_element(by=By.XPATH, value='//input[@name="login_name"]'):
  
    username_input = driver.find_element(by=By.XPATH, value='//input[@name="login_name"]')
    # password = driver.find_element(By.ID, 'login_password')
    password_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    # button = driver.find_element(By.NAME, '登录')
    button = driver.find_element(by=By.CLASS_NAME, value='btn')
    username_input.send_keys(box_username)
    password_input.send_keys(box_password)
    button.click()
    """
    global plm_opened_flag
    if plm_opened_flag:
        # 开新tab,对窗口发送“control+t”组合键
        driver.find_element(by=By.XPATH, value='//body').send_keys(Keys.CONTROL + 't')
        driver.get(leiQu_url)
    else:
        driver.get(leiQu_url)  # 此时打开的是PLM的首页
        driver.get(leiQu_url)
        plm_opened_flag = True
    time.sleep(1)
    product_select = Select(driver.find_element(by=By.XPATH, value='//select[@title="产品线"]'))
    product_select.select_by_value("BOX")
    search_button = driver.find_element(by=By.XPATH, value='//input[@value="查询"]')
    search_button.click()
    
    
def open_rc_url():
    # box_username = login.main_ui.lineEdit.text()
    # box_password = login.main_ui.lineEdit_2.text()
    search_word = guide.child.lineEdit.text()
    
    # driver = webdriver.Firefox()
    '''
    driver.get(plm_url)
    username_input = driver.find_element(by=By.XPATH, value='//input[@name="login_name"]')
    password_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    button = driver.find_element(by=By.CLASS_NAME, value='btn')
    username_input.send_keys(box_username)
    password_input.send_keys(box_password)
    button.click()
    '''
    global plm_opened_flag
    if plm_opened_flag:  # 打开过PLM，就只用打开一次url，否则要打开2次，第一次是打开PLM首页
        driver.get(rc_url)
    else:
        driver.get(rc_url)
        driver.get(rc_url)
        plm_opened_flag = True
        # driver.get(rc_url)
        #切换到输入框的frame，直接打开rc_url，就没有上层的iframe了
        # frame = driver.find_element(by=By.XPATH, value='//iframe[@name="content"]')
        # driver.switch_to.frame(frame)
        # driver.switch_to.frame("content")
        # driver.switch_to.frame("portalDisplay")
        # driver.switch_to.frame("HBMTPriorityLibraryParts")
    driver.switch_to.frame("listFilter")
    res_input = driver.find_element(by=By.XPATH, value='//input[@name="filterResistance"]')
    cap_input = driver.find_element(by=By.XPATH, value='//input[@name="filterCapacity"]')
    search_button = driver.find_element(by=By.XPATH, value='//input[@value="全库搜索"]')
    word_filter = "".join([i for i in search_word if (not i.isdigit() and i != ".")])
    dict_slope = {'pF': 1e-6, 'PF': 1e-6, 'pf': 1e-6, 'Pf': 1e-6, 'nF': 1e-3, 'NF': 1e-3, 'nf': 1e-3, 'Nf': 1e-3,
                 'uF': 1, 'UF': 1, 'uf': 1, 'Uf': 1, 'k': 1e+3, 'K': 1e+3, 'm': 1e+6, 'M': 1e+6}
    if word_filter:  # 如果输入带单位
        search_num = search_word.replace(word_filter, "", 1)    
        search_num_real = float(search_num) * dict_slope[word_filter]  # int 不能直接与float计算
        if dict_slope[word_filter] <= 1:
            cap_input.send_keys('{:9f}'.format(search_num_real).rstrip('0'))
            search_button.click()
        else:
            res_input.send_keys(search_num_real)
            search_button.click()
    else:
        res_input.send_keys(search_word)
        search_button.click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to.frame("listDisplay")
    sort_button = driver.find_element(by=By.XPATH, value='//a[contains(text(), "推荐使用物料")]')
    sort_button.click()
    time.sleep(1)
    # 点击一次后url刷新，需要再找一次
    sort_button = driver.find_element(by=By.XPATH, value='//a[contains(text(), "推荐使用物料")]')
    sort_button.click()

    
def open_bom_download_url():
    return


def lock_window():
    if guide.window_locked:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("unlock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lock_button.setIcon(icon)
        guide.setWindowFlags(guide.defaultWindowFlag)
        guide.setVisible(True)  # 改板窗体属性后，需要重新让它可见
        '''
        h1 = guide.frameGeometry().height()
        h_offset = h1 - guide.height()
        guide.move(guide.x(), guide.y() - h_offset)
        '''
        guide.window_locked = False
    else:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lock_button.setIcon(icon)
        guide.setWindowFlags(guide.defaultWindowFlag | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # setWindowFlags时，参数必须与defaultWindowFlag 或运算，不然会改变windowFlag的其他属性，比如位置
        guide.setVisible(True)
        guide.window_locked = True
        
        
def guide_show():
    loginBtn.setText("登录中...")  # 这样setText不会在已生产的GUI改变按钮文本
    box_username = login.main_ui.lineEdit.text()
    box_password = login.main_ui.lineEdit_2.text()
    # code_name = base64.b64encode(box_username.encode('utf-8'))  # 必须要encode成byte变量，string变量无法加密
    code_name = base64.b64encode(box_username.encode('utf-8'))
    code_psw = base64.b64encode(box_password.encode('utf-8'))
    if login.main_ui.checkBox.isChecked():
        with open("config.txt", "w") as fp:
            config = {'name': code_name.decode('utf-8'), 'psw': code_psw.decode('utf-8')}
            json.dump(config, fp)
            fp.close()

    # web_option = Options()
    # web_option.add_argument('-headless')  # 无头参数，加入此参数不显示网页    
    # driver = webdriver.Firefox(options=web_option)
    
    driver.get(sso_url)  # 打开sso平台登录页面
    # 找到登录界面的用户名，密码输入框和登录按钮    
    username_input = driver.find_element(by=By.XPATH, value='//input[@id="_username_username"]')
    password_input = driver.find_element(by=By.XPATH, value='//input[@id="_username_password"]')
    button = driver.find_element(by=By.XPATH, value='//div[@id="usernamaSubmit"]')
    '''
    driver.get(plm_url)
    username_input = driver.find_element(by=By.XPATH, value='//input[@name="login_name"]')
    password_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    button = driver.find_element(by=By.CLASS_NAME, value='btn')
    '''
    username_input.send_keys(box_username)
    password_input.send_keys(box_password)
    button.click()    
    driver.minimize_window()
    if EC.alert_is_present()(driver):
        time.sleep(2)
        driver.switch_to.alert.accept()
        driver.quit()
    else:
        time.sleep(1)
        cookies = driver.get_cookies()  # 获取SSO登录的cookie，方便打开其他平台
        with open("cookies.txt", "w") as fp:
            json.dump(cookies, fp)
        # driver.quit()  # 无头打开url后，需要quit再重新用有头的option打开，才能重新显示页面
    login.hide()
    guide.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 初始化变量
    plm_opened_flag = False
    # 把driver初始化放在main里
    driver = webdriver.Firefox()
    # 获取桌面属性
    desktop = QApplication.desktop()
    login = LoginWindow()
    guide = RD_GuideWindow()
    connect = ConnectWindow()
    # availableGeometry()是屏幕除任务栏外的尺寸
    # guide_y = (desktop.availableGeometry().height() - login.frameSize().height()) // 2
    # 调整窗口显示位置
    # login.move(30, guide_y)
    guide.move(login.frameSize().width() + 32, 0)
    loginBtn = login.main_ui.pushButton
    # 保存登录cookies
    loginBtn.clicked.connect(guide_show)
    # 研发案例搜索窗口打开，
    guideModePushButton = guide.child.pushButton
    guideModePushButton.clicked.connect(open_leiQu_url)

    # 阻容物料等级库打开
    rc_searchToolButton = guide.child.toolButton
    rc_search = guide.child.lineEdit
    rc_search.returnPressed.connect(open_rc_url)  # 输入完成后按回车搜索
    rc_searchToolButton.clicked.connect(open_rc_url)
    # BOM下载页面打开
    bom_searchToolButton = guide.child.toolButton
    bom_search = guide.child.lineEdit_2
    bom_search.returnPressed.connect(open_bom_download_url)  # 输入完成后按回车搜索
    bom_searchToolButton.clicked.connect(open_bom_download_url)
    
    # 靠边隐藏
    # guide.mouseGrabber()
    # 锁定和解锁窗口栏的按钮

    lock_button = guide.child.pushButton_2
    lock_button.clicked.connect(lock_window)
    
    try:
        with open("config.txt", "r") as fp:
            config = json.load(fp)
            realName = base64.b64decode(config['name'])
            realPsw = base64.b64decode(config['psw'])
            login.main_ui.lineEdit.setText(str(realName, 'utf-8'))
            login.main_ui.lineEdit_2.setText(str(realPsw, 'utf-8'))
            login.show()
    except Exception as e:
        login.show()
    sys.exit(app.exec())
        
    
              
       
  
  
    
