from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

ROOT_TAG = "Segments"
REALTIME_TAG = "RealTime"
GAMETIME_TAG = "GameTime"

def convert(timef)->str:
    timef = timef.split(".")
    if len(timef)> 1:
        timef[-1] = timef[-1][:6].ljust(6, '0')
    else:
        timef.append("".ljust(6, '0'))
    timef = '.'.join(timef) 
    time = datetime.strptime(timef, "%H:%M:%S.%f").time()
    conversion_constant = (60 / 59.7275)
    total_seconds = round((time.hour * 3600 + time.minute * 60 + time.second + time.microsecond / 1000000) * conversion_constant,3)
    converted_time = (datetime.min + timedelta(seconds=total_seconds)).time()
    newtime = str(converted_time)
    return newtime


def parse_gametime(file_path:str):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for element in root.findall(f'.//{ROOT_TAG}')[0].iter():
        if element.tag == REALTIME_TAG:
            converted_text = convert(element.text)
        elif element.tag == GAMETIME_TAG:
            element.text = converted_text
    return ET.tostring(root, encoding='utf-8').decode('utf-8')

file_path = "input.lss"
res = parse_gametime(file_path)

open("output.lss", "w").write(res)
