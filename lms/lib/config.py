from pathlib import Path


def Config():
    _configFile = Path(__file__).parent.parent.resolve()
    _configFile = str(_configFile)  + "\config.init"

    configurationData = {}

    with open(_configFile, "r") as config:
        configData = config.readlines()
        for data in configData:
            if "#" not in data:
                _configData = data.strip().split("=")
                configurationData.update({_configData[0]: _configData[1]})

    return configurationData