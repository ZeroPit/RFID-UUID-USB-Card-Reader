import uuidreader

print('Get all devices and print with debug=True')
device_list = uuidreader.list_devices(debug=True)

print('Or print from list')
for single_device in device_list:
    print(
        'fn: ' + str(single_device['fn']),
        'name: ' + str(single_device['name']),
        'phys: ' + str(single_device['phys'])
        )
