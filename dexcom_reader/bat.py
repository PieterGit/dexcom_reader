
# turn off dexcom charging

from read_data import Dexcom
class DexcomBattery(Dexcom):
    @classmethod
    def LocateAndDownload(cls):
        device = cls.FindDevice()
        if not device:
            sys.stderr.write('Could not find Dexcom Receiver!\n')
            sys.exit(1)
        else:
            dex = cls(device)
            dex.WriteChargerCurrentSetting ('Off')
        print 'Battery Status: %s (%d%%)' % (dex.ReadBatteryState(),
                                           dex.ReadBatteryLevel())
        print 'Battery Charge Current Setting: %s' % dex.ReadChargerCurrentSetting()

if __name__ == '__main__':
  DexcomBattery.LocateAndDownload()
