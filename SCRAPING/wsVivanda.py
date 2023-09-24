from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DTO.RegistroPrecioDTO import RegistroPrecioDTO
from DTO.SimilarDTO import SimilarDTO

from Service import RestServiceClient

from SCRAPING.wsBase import wsBase

class wsVivanda(wsBase):

    def BusquedaEspecifica(self, similar : SimilarDTO, webDriver : webdriver.Firefox, nIdExecutionBot):
        self.initWebDrivers(similar.sUrl, waitTime=1, webDriver=webDriver)
        precio = ''
        precioO = ''
        precioT = ''

        if (self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[2]/span')
                and webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[2]/span').get_attribute('class').__contains__('vivanda-product-price-1-x-listPrice')
            ):
                precio = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[2]/span/span/span').text.split('/')[1].replace(',','')
                precioO = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[3]/div/div/div[1]/span/span/span').text.split('/')[1].replace(',','')
        elif(self.existeElementoWDT(webDriver, 2, By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[3]/div/div/div[1]/span/span/span')
                and webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[3]/div/div/div[1]/span/span/span').text != ''
            ):
            precio = webDriver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div[3]/div/section/div/div[2]/div/div[4]/div/div/div/div/div[3]/div/div/div[1]/span/span/span').text.split('/')[1].replace(',','')

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