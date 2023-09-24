from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DTO.RegistroPrecioDTO import RegistroPrecioDTO
from DTO.SimilarDTO import SimilarDTO

from Service import RestServiceClient

from SCRAPING.wsBase import wsBase

class wsPlazaVea(wsBase):

    def BusquedaEspecifica(self, similar : SimilarDTO, webDriver : webdriver.Firefox, nIdExecutionBot):
        self.initWebDrivers(similar.sUrl, waitTime=1, webDriver=webDriver)
        precio = ''
        precioO = ''
        precioT = ''

        if (self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[5]')
                and webDriver.find_element(By.XPATH, '/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[5]').get_attribute('class') == 'ProductCard__price ProductCard__price--oh'
            ):
            precioT = webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[5]/div[1]').text.split('/')[1].replace(',','')

        if (self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[2]')
                and webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[2]').get_attribute('class') == 'ProductCard__price ProductCard__price--regular'
            ):
                precio = webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[2]/div').text.split('/')[1].replace(',','')
                precioO = webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]').text.split('/')[1].replace(',','')
        elif(self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]')
                and webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]').text != ''
            ):
            precio = webDriver.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[1]/div[3]/div[2]/div[2]/div[3]/div[3]/div[1]').text.split('/')[1].replace(',','')

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
        
