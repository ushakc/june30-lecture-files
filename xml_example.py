import xml.etree.ElementTree as ET
import re

tree = ET.parse('/Users/samanthagrzegorzewski/movies.xml')
root = tree.getroot()

#print(root.tag)
#print([elem.tag for elem in root.iter()])

for child in root:
    #print(child.tag, child.attrib)
    pass
    
#print([elem.tag for elem in root.iter()])

#cprint(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    pass
    #print(movie.attrib)
    

for description in root.iter('description'):
    #print(description.text)
    pass

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    #print(movie.attrib)
    pass
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    #print(movie.attrib)
    pass

for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    #print(movie.attrib)
    pass

for movie in root.iter('movie'):
    #print(movie.attrib)
    pass

#b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
#print(b2tf)

#b2tf.attrib['title'] = 'Back to the Future'
#print(b2tf.attrib)

#tree.write("movies.xml")

#tree = ET.parse('movies.xml')
#root = tree.getroot()

for movie in root.iter('movie'):
    #print(movie.attrib)
    pass

for form in root.findall("./genre/decade/movie/format"):
    #print(form.attrib, form.text)
    pass

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(r',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')
        
tree.write("movies.xml")

for form in root.findall("./genre/decade/movie/format"):
    #print(form.attrib, form.text)
    pass

for decade in root.findall("./genre/decade"):
    #print(decade.attrib)
    for year in decade.findall("./movie/year"):
        #print(year.text, '\n')
        pass
        
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    #print(movie.attrib)
    pass

action = root.find("./genre[@category='Action']")
#print(action)
new_dec = ET.SubElement(action, 'decade')
#print(new_dec)
new_dec.attrib["years"] = '2000s'

#print(ET.tostring(action, encoding='utf8').decode('utf8'))

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

#print(ET.tostring(action, encoding='utf8').decode('utf8'))
tree.write("movies.xml")