import os
import shutil
from PHM_UtilityTools import updatemanager
def upgrade_UpdateManager():
    src = "temp_usr/Phantom_Toolbox-main/PHM_UtilityTools/updatemanager.py"
    dst = "PHM_UtilityTools/updatemanager.py"
    os.remove(dst)
    shutil.copy2(src, dst)
    updatemanager.sudo(0)
