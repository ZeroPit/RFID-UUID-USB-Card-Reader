import uuidreader

uuidreader.list_devices(True)
device_id = input('Choose the USB Card Reader device /dev/input/event[ID]: ')
print('USB Card Reader use device %s' % device_id)

uuid = uuidreader.read(device_id)
print('Read uuid: ' + str(uuid))
