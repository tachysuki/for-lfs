ORANGE = "\033[38;2;237;85;27m"
END = "\033[0m"
CHAR = [ORANGE + "ooooooooooo ooooooooooo  ooooooo  oooo   oooo ooooo  oooooooo8" + END,
        ORANGE + "88    888    888    88 o888   888o 8888o  88   888 o888     88" + END,
        ORANGE + "    888      888ooo8   888     888 88 888o88   888 888"         + END,
        ORANGE + "  888    oo  888    oo 888o   o888 88   8888   888 888o     oo" + END + " Heavy Industries",
        ORANGE + "o888oooo888 o888ooo8888  88ooo88  o88o    88  o888o 888oooo88 " + END + " MSBIOS Revision 0613(KB)" + END,
                 "MS-06 MS Component",
                 "   - Manufacture Code: ZIII-MS-06-????",
                 "     Firmware Build: UNKNOWN",
                 "   - Last Maintenaunce: DATA CORRUPTED",
                 "",
                 "",
                 "",
                 "Primary Boot DEVICE: Detected",
                 "   - Authentication: DYPA33ED",
                 "     Boot Sequence: INITIALIZED (WARNING: UNVERFIED)",
                 "Actuvation: OK",
                 "Connection: OK",
                 "Limmitter: UNLOCKED (WARNING: SECURITY OVERRIDE DETECTED)",
                 "",
                 "",
                 "Fire Control System: OK",
                 "   - Weapon Calibration: ERROR (FALLBACK MODE)",
                 "   - Targeting Sensors: ONLINE",
                 "   - Ammunition Status: PARTIAL DATA AVAILABLE",
                 "","","","","","",""]

for i in range(0,len(CHAR)):
    print(CHAR[i])