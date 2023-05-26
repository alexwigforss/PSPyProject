from readimages import getTxtFileNames as gtf
import os
longpath = os.getcwd() + '\\' + 'text\\'
path = '.\\text\\'
textfiles = gtf()
listoflines = []
lines = ''
for e in textfiles:
    print(path + e)
    with open(path + e, encoding='utf-8') as f:
        listoflines.append(f.read())

nextValue = False
label_list = ['grobarhet:','Radavstand:','Plantavstand:','SkOrdas:','Portion:','Satid:']
for text in listoflines:
    for word in enumerate(text.split()):
        if nextValue:
            print(label,word[1])

        if word[1] in label_list:
            label = word[1][0:4]
            nextValue = True
        else:
            nextValue = False
    print()

thisdict = {
  "grobarhet": 0,
  "Radavstand": 0,
  "Plantavstand": 0,
  "SkOrdas": "unset",
  "Portion": 0,
  "Satid": "unset",
}

"""
grobarhet: 75%
Radavstand: 50cm
Plantavstand: 50 cm
SkOrdas: aug-sep
Portion: 10 fro
Satid: feb-april

Radavstand: 50cm
Plantavstand: 50 cm 
SkOrdas: aug-sep 
Portion: 10 fro
\nCucumis melo *Honey Dew’  Lust grénvita, runda-ovala frukter pa ca 1 kg. Sétt, saftigt, Appelgront fruktkott med ett latt krisp. Popular dessertfrukt, pa exotisk bricka eller i fruktsallad m.m. ¢ ’  Odling: Frkultiveras inomhus i planteringsjord. Hall sédden vid ca25 grader, efter groning ca 20 grader. Varmekravande. Odlas i vaxthus éller bank. Nyp av vid tillvaxtpunkten pa huvudstammen efter 5-7 blad och sidoskotten efter 2-3 blad. Uppbindes eller markodlas. Blommoma handpolline- ras med pensel. Mogna frukter doftar melon och stjalken spricker vid fruktfastet. }  \n'

"""