from creational.factory_method.logistics.air_logistic import AirLogistic
from creational.factory_method.logistics.sea_logistic import SeaLogistic


def process(logistic_type):
    try:
        logistic = {
            "sea": SeaLogistic,
            "air": AirLogistic,
        }[logistic_type]
    except KeyError:
        raise NotImplementedError("This type of logistics has not been implemented yet.")

    return logistic().start_expedition()
