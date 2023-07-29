import wmi
data = wmi.WMI()
for os_name in data.Win32_OperatingSystem():
    print(os_name.Caption) # Microsoft Windows 11 Home