import pykakasi

kakasi = pykakasi.kakasi()
kakasi.setMode('H', 'a')
conversion = kakasi.getConverter()

if __name__ == '__main__':
    print(conversion.do('おはよう'))
    print(conversion.do('おやすみ'))
    print(conversion.do('ごめんね'))
    print(conversion.do('おつかれ'))
    
# end of line break
