from guns.defaultGun import DefaultGun

class GunFactory:

    @staticmethod
    def create(gun_code):
        match gun_code:
            case "default":
                return DefaultGun()
        return False