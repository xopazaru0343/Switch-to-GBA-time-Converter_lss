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
nf = open('tempfileconvert', 'w')

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

# Gambiarra/Workaround
f.close() 
f2 = open('Metroid Zero Mission - Any_ (Easy).lss', 'r+', encoding="utf-8")
lines = f2.readlines()
index_ct = 0 
for line in lines: 
    nf.write(line)
    if (line.lstrip()).startswith('<RealTime>'): 
        nf.write(" " * line.count(" ") + f"<GameTime>{converted_times[index_ct]}0000</GameTime>\n")
        if index_ct < len(converted_times) - 1:
            index_ct += 1
f2.close() 
nf.close()

# Writing the changes
f = open('Metroid Zero Mission - Any_ (Easy).lss', 'w', encoding="utf-8")
f2 = open('tempfileconvert', 'r')
text = f2.read()
f.write(text)
f.close()
f2.close()



# Debugger de pobre
#f.write(text) 
#f.close() 
#print(text)
#print(base_times)
#print(converted_times)
#print(float7_formatted)
#print(lines)
