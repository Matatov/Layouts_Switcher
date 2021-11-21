import os
counter = os.popen("powershell Get-WinUserLanguageList").read().count("LanguageTag")
if counter == 3:
    os.system("powershell Set-WinUserLanguageList -LanguageList en-US, ru -Force")
else:
    os.system("powershell Set-WinUserLanguageList -LanguageList en-US, ru, he -Force")
