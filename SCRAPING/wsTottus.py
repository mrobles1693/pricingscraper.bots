from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DTO.RegistroPrecioDTO import RegistroPrecioDTO
from DTO.SimilarDTO import SimilarDTO

from Service import RestServiceClient

from SCRAPING.wsBase import wsBase

class wsTottus(wsBase):

    def BusquedaEspecifica(self, similar : SimilarDTO, webDriver : webdriver.Firefox, nIdExecutionBot):
        self.initWebDrivers(similar.sUrl, waitTime=1, webDriver=webDriver)

        WebDriverWait(webDriver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section/div[1]/div[2]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li[1]')))

        precio = ''
        precioO = ''
        precioT = ''

        if(self.existeElementoWD(webDriver,By.XPATH,'/html/body/div[1]/div/section/div[1]/div[2]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li[2]/div/span')):
            precioO = webDriver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[1]/div[2]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li[1]/div/span').text
            precio = webDriver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[1]/div[2]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li[2]/div/span').text
        else:
            precio = webDriver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[1]/div[2]/div[2]/section[2]/div[2]/div/div[2]/div[1]/div[1]/ol/li[1]/div/span').text

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
        print(res)
        