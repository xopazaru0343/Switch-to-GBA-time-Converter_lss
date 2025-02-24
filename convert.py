import re 
    
def convert(timef):
    conversion_constant = (60 / 59.7275)
    run = timef
    h = int(run.split(':')[0])
    m = int(run.split(':')[1])
    s = int(run.split(':')[2].split('.')[0])
    ms = int(run.split('.')[1])

    original = h * 3600 + m * 60 + s + (ms / 1000)

    converted = round(original * conversion_constant, 3)

    newtime = str(converted)

    newms = int(newtime.split('.')[1])

    newseconds = int(newtime.split('.')[0])
    news = newseconds % 60
    newseconds -= news

    newm = (newseconds % 3600) / 60
    newm = int(newm)

    newh = newseconds - (newm * 60)
    newh /= 3600
    newh = int(newh)

    newtime = f'{newh:02d}:{newm:02d}:{news:02d}.{newms:03d}' 
    return newtime 
    
f = open('Metroid Zero Mission - Any_ (Easy).lss', 'r+', encoding="utf-8") 

# Time conversion

text = f.read() 
pattern = r"([0-9]{2}:[0-9]{2}:[0-9]{2})(\.[0-9]{1,3})"  
brute_time = re.findall(pattern, text) 
base_times = [] 
converted_times = [] 

for i in range(len(brute_time)):
    base_times.append(re.sub(r"[\s,')(]", '', str(brute_time[i]))) 

for i in range(len(base_times)): 
    new_time = convert(base_times[i])
    converted_times.append(new_time) 

for i in range(len(converted_times)): 
    text = re.sub(base_times[i], converted_times[i], text)  

# Time formatting

pattern2 = r"([0-9]{2}:[0-9]{2}:[0-9]{2})(\.[0-9]{1,7})" 
float7_brute = re.findall(pattern2, text)
float7_formatted = []
for i in range(len(float7_brute)):
    float7_formatted.append(re.sub(r"[\s,')(]", '', str(float7_brute[i]))) 

for i in range(len(float7_formatted)): 
    a = float7_formatted[i] 
    text = re.sub(float7_formatted[i], a[0: 12] + '0000', text) 

f.write(text) 
f.close() 
print(text)

