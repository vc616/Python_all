import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities  import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {
    'browser':'ALL',
    'performance':'ALL',
}
caps['perfLoggingPrefs'] = {
    'enableNetwork' : True,
    'enablePage' : False,
    'enableTimeline' : False
    }

option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')
option.add_argument("--disable-extensions")
option.add_argument("--allow-running-insecure-content")
option.add_argument("--ignore-certificate-errors")
option.add_argument("--disable-single-click-autofill")
option.add_argument("--disable-autofill-keyboard-accessory-view[8]")
option.add_argument("--disable-full-form-autofill-ios")
option.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:55.0) Gecko/20100101 Firefox/55.0')
option.add_experimental_option('w3c',False)
option.add_experimental_option('perfLoggingPrefs',{
    'enableNetwork':True,
    'enablePage':False,
})
driver = webdriver.Chrome(options=option,desired_capabilities=caps)
driver.get('http://www.foo.com/')
for typelog in driver.log_types:
    perfs = driver.get_log(typelog)
    for row in perfs:
        log_data = row
        log_json = json.loads(log_data['message'])
        log = log_json['message']
        if log['method'] == 'Network.responseReceived':
            requestId = log['params']['requestId']
            try:
                response_body = driver.execute_cdp_cmd('Network.getResponseBody',{'requestId': requestId})
                print(response_body['body'])

            except:
                print('response.body is null')
