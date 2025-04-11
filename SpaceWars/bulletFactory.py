from bullets.defaultBullet import DefaultBullet

class BulletFactory:

    @staticmethod
    def create(bullet_code):
        match bullet_code:
            case "default":
                return DefaultBullet()
        return False
