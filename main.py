
from DTO.SimilarDTO import SimilarDTO
from DTO.SqlRspDTO import SqlRspDTO
from SCRAPING.wsTottus import wsTottus
from SCRAPING.wsVivanda import wsVivanda
from SCRAPING.wsWong import wsWong
from Service import RestServiceClient
from SCRAPING.wsPlazaVea import wsPlazaVea
from selenium import webdriver

if __name__ == '__main__':
    iniRes = RestServiceClient.iniBotExecution()
    if(iniRes.success):
        nIdExecutionBot = SqlRspDTO().from_json(iniRes.data).nCod

        res = RestServiceClient.getListSimilar()
        if(res.success):
            
            wdp = webdriver.Firefox()

            for d in res.data:
                wdp.get('https://www.google.com')
                similar = SimilarDTO().from_json(d)
                if(similar.nIdComercio == 1):
                    wsTottus().BusquedaEspecifica(similar=similar, webDriver=wdp, nIdExecutionBot=nIdExecutionBot)
                if(similar.nIdComercio == 2):
                    wsPlazaVea().BusquedaEspecifica(similar=similar, webDriver=wdp, nIdExecutionBot=nIdExecutionBot)
                if(similar.nIdComercio == 3):
                    wsVivanda().BusquedaEspecifica(similar=similar, webDriver=wdp, nIdExecutionBot=nIdExecutionBot)
                if(similar.nIdComercio == 4):
                    wsWong().BusquedaEspecifica(similar=similar, webDriver=wdp, nIdExecutionBot=nIdExecutionBot)

        finRes = RestServiceClient.finBotExecution(nIdExecutionBot)