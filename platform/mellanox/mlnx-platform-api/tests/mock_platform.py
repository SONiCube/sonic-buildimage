class MockFan:
    def __init__(self):
        self.presence = True
        self.speed = 60

    def get_presence(self):
        return self.presence

    def set_speed(self, speed):
        self.speed = speed


class MockPsu:
    def __init__(self):
        self.presence = True
        self.powergood = True

    def get_presence(self):
        return self.presence

    def get_powergood_status(self):
        return self.powergood


class MockChassis:
    def __init__(self):
        self.fan_list = []
        self.psu_list = []

    def get_all_psus(self):
        return self.psu_list

    def get_all_fans(self):
        return self.fan_list

    def get_thermal_manager(self):
        from sonic_platform.thermal_manager import ThermalManager
        return ThermalManager

    def make_fan_absence(self):
        fan = MockFan()
        fan.presence = False
        self.fan_list.append(fan)

    def make_psu_absence(self):
        psu = MockPsu()
        psu.presence = False
        self.psu_list.append(psu)
