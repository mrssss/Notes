import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler:
    def __init__(self, provinces):
        self.provinces = provinces

    def start_handler(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    def end_handler(self, name):
        pass

    def char_data(self, text):
        pass

def get_province_entry(url):
    pass
    content = requests.get(url).content.decode('gb2312')
    start = content.find('<map name="map_86" id="map_86">')
    end = content.find('</map>')
    content = content[start : end + len('</map>')].strip()

    provinces = []    
    handler = DefaultSaxHandler(provinces)
    parse = ParserCreate()
    parse.StartElementHandler = handler.start_handler
    parse.EndElementHandler = handler.end_handler
    parse.CharacterDataHandler = handler.char_data
    parse.Parse(content)
    return provinces
    # print(content)

provinces = get_province_entry('http://www.ip138.com/post')
print(provinces)
