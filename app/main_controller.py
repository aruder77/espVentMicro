from esp_micro.esp_micro_controller import EspMicroController
from espvent_device import EspVentDevice


class MainController(EspMicroController):
    def __init__(self):
        super().__init__()

    def createHomieDevice(self, settings):
        return EspVentDevice(settings)

    def getDeviceName(self):
        return 'espVentuMicro'

    def getDeviceID(self):
        return 'espVentuMicro'
