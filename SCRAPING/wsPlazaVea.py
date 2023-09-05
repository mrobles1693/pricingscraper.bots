import selenium

from SCRAPING.wsBase import wsBase

class wsPlazaVea(wsBase):

    def BusquedaEspecifica(self, similar, webDriver):
        self.initWebDrivers(similar.sUrl, waitTime=1, webDriver=webDriver)