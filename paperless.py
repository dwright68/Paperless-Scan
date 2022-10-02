from pywinauto.application import Application
import time
from datetime import datetime

now = datetime.now().strftime("%I-%M-%S")

# start scan appand wait for it to open
app = Application(backend='win32').start(r"installation\dir\HP\HP LaserJet Pro MFP M25-M27\bin\HPScan.exe")
time.sleep(20)

# this finds and clicks the scan button then waits for the scan to finish
dlg = app.top_window()
dlg.ScanButton.click()
time.sleep(30)

# finds the save as window and enters the name with the time appended.
save_dlg = app.window(title="Save As")
save_dlg.FileNameComboBox.type_keys(f"scan_{now}")
save_dlg.SaveButton.click()
dlg.CancelButton.click()