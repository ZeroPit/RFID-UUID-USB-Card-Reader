
RFID-UUID-USB-Card-Reader
=========================

Hardware
========
USB RFID DeskTop ID Kartenlesegerät

Install
=======
pip install RFID-UUID-USB-Card-Reader


Der RFID Reader
===============
Es gibt die Funktionen
* list_devices(debug=false)
   * Listet alle Devices auf
* init_divice(device_id, debug=False):
   * Gibt das ausgewählte Device zurück device_id= [1,2,..,X]
* read(device_id, debug=false)
   * List vom Device den RFID Tag und gibt eine UUID zurück
* read_rfid_reader(device_id, debug=false)
   * List vom Device den RFID Tag und gibt diesen zurück


