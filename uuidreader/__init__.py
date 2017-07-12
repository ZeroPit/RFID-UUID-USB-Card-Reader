# -*- coding: utf-8 -*-
#!/usr/bin/env python

# uuidreader.py

import evdev

import utils

rfidcodes = {2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8', 10: u'9', 11: u'0'}

Device = None

def init_divice(device):
    try:
        Device = evdev.InputDevice('/dev/input/event' + str(device))
        print(Device)
        return True
    except:
        print('No Devices file found')
        return False

def read_rfid_reader(debug=False):
    print('Read RFID form USB Card Reader')
    rfid_code = ''
    if Device is None:
        init_divice()
    if Device is not None:
        for event in Device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                # Nur beim Key_Down
                if event.value == 1:
                    if event.code == 28:
                        return rfid_code
                    else:
                        rfid_code += rfidcodes[event.code]
    return rfid_code

def list_devices(debug=False):
    """
    List all connectet devices and wirte the importen information in a list
    :param debug: if True print debug msg
    :return: return a list of all usb devices
    """
    device_list = list()
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    if len(devices) == 0:
        utils.debug_print('No Devices found', debug)
        return list()
    for device in devices:
        utils.debug_print(str(device.fn) + ' ' + device.name + ' ' + str(device.phys), debug)
        device_list.append(
            {
                'fn': device.fn,
                'name': device.name,
                'phys': device.phys
            }
        )
    return device_list


def read(debug=False):
    """Read from the card Reader

    :param debug: if True print debug msg
    :return:  return the reading UUID
    """
    rfid_code = read_rfid_reader(debug)
    rfid_uuid = utils.rfid_code_to_uuid(rfid_code, debug)
    utils.debug_print('RFID as UUID: ' + rfid_uuid, debug)
    return rfid_uuid
