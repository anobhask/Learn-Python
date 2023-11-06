# list services
import wmi
conn = wmi.WMI()
for s in conn.Win32_Service(StartMode="Auto", State="Running"):
# filter service names
   if 'Update' in s.Name:
        print(s.State, s.StartMode, s.Name, s.DisplayName)
# list processes
conn = wmi.WMI()
for process in conn.Win32_Process():
    print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
    process.ProcessId, process.HandleCount, process.Name))
print(conn.classes)