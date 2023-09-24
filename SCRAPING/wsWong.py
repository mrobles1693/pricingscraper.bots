from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DTO.RegistroPrecioDTO import RegistroPrecioDTO
from DTO.SimilarDTO import SimilarDTO

from Service import RestServiceClient

from SCRAPING.wsBase import wsBase

class wsWong(wsBase):

    def BusquedaEspecifica(self, similar : SimilarDTO, webDriver : webdriver.Firefox, nIdExecutionBot):
        self.initWebDrivers(similar.sUrl, waitTime=1, webDriver=webDriver)
        precio = ''
        precioO = ''
        precioT = ''
        
        if (self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[7]/div/p/span')
                and webDriver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[7]/div/p/span').get_attribute('class').__contains__('wongio-wongiocompo1app-0-x-prime-price')
            ):
            precioT = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[7]/div/p/span/span').text.split('/')[1].replace(',','')

        if (self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[9]/span/span')
                and webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[9]/span/span').get_attribute('class').__contains__('vtex-product-price-1-x-listPriceValue')
            ):
                precio = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[9]/span/span/span').text.split('/')[1].replace(',','')
                precioO = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[8]/span/span/span').text.split('/')[1].replace(',','')
        elif(self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[8]/span/span/span')
                and webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[8]/span/span/span').text != ''
            ):
            precio = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/section/div/div[2]/div/div[8]/span/span/span').text.split('/')[1].replace(',','')

        if(precio != ''):
            registroPrecio = RegistroPrecioDTO(
                nIdBotExecution=nIdExecutionBot
                ,nIdSimilar=similar.nIdSimilar
                ,nIdComercio=similar.nIdComercio
                ,nIdProducto=similar.nIdProducto
                ,nPrecio= float(precio.replace('S/ ','')) if precio != '' else None
                ,nPrecioOferta= float(precioO.replace('S/ ','')) if precioO != '' else None
                ,nPrecioTarjeta= float(precioT.replace('S/ ','')) if precioT != '' else None
                ,dFecha=None
                ,nIdRegistroPrecio=None
            )

            res = RestServiceClient.insRegistroPrecio(registroPrecio=registroPrecio)