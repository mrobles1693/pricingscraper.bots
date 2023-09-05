from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class wsBase:

    @abstractmethod
    def BusquedaEspecifica(similar, webDriver):
        pass
    
    def initWebDrivers(self, url, waitTime, webDriver):
        self.wdPrincipal = webDriver
        self.wdwPrincipal = WebDriverWait(self.wdPrincipal, waitTime)
        self.wdPrincipal.maximize_window()
        self.wdPrincipal.get(url)

    def existeElemento(driver, by, valor):
        try:
            driver.find_element(by, valor)
            return True
        except:
            return False
        
    def existeElemento(webElement, by, valor):
        try:
            webElement.find_element(by, valor)
            return True
        except:
            return False
        
    def existeElemento(wait, by, valor):
        try:
            wait.until(EC.presence_of_element_located((by, valor)))
            return True
        except:
            return False
    
    def existeElemento(wd, tiempo, by, valor):
        try:
            wait = WebDriverWait(wd, tiempo)
            wait.until(EC.presence_of_element_located((by, valor)))
            return True
        except:
            return False
    
    def generateXpath(self, cwe, current) -> str:
        childTag = cwe.tag_name
        if(childTag == 'html'):
            return 'html[1]' + current
        
        parentElement = cwe.find_element(By.XPATH,'..')
        childrenElements = parentElement.find_element(By.XPATH,'*')
        count = 0
        for ce in childrenElements:
            ceTag = ce.tag_name
            if(childTag == ceTag):
                count += 1
            if(ce.equals(cwe)):
                return self.generateXpath(parentElement, '/' + ceTag + '['+count+']'+current)
        
        return ''
            