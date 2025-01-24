import pandas as pd


surnames = pd.read_csv('surnames.csv')
xy = pd.read_csv('maleFirstNames.csv')
xx = pd.read_csv('femaleFirstNames.csv')

snames=[col for col in surnames.columns]
m_fnames=[]
f_fnames=[]

for name in xy:
    m_fnames.append(name.replace(u'\xa0', ''))

for name in xx:
    f_fnames.append(name.replace(u'\xa0', ''))
    # print(name)


familyList=[]
counter = 1
nIndex = 1

while counter <= 996 and nIndex <= 49:
    for s in snames:
        familyDict = {}

        # familyDict['Family_Name'] = s
        if counter % 19 == 0 and nIndex + 2 <= len(m_fnames)-1:
            familyDict['Father'] = m_fnames[nIndex] + ' ' + s
            familyDict['Mother'] = f_fnames[nIndex] + ' ' + s
            familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
            familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s

            if counter % 2 == 0 and counter < 49:
                familyDict['Son2'] = m_fnames[nIndex + 2] + ' ' + s

            elif counter % 3 == 0 and counter < 49:
                familyDict['Daughter2'] = f_fnames[nIndex + 2] + ' ' + s

            else:
                familyDict['Son2'] = m_fnames[nIndex + 2] + ' ' + s
                familyDict['Daughter2'] = f_fnames[nIndex + 2] + ' ' + s


        elif counter % 23 == 0 and nIndex + 2 <= len(m_fnames)-1:
            familyDict['Father'] = m_fnames[nIndex]+ ' ' +s
            familyDict['Mother'] = f_fnames[nIndex]+ ' ' +s

            if counter % 5 == 0:
                familyDict['Son'] = m_fnames[nIndex + 2]+ ' ' +s

            else:
                familyDict['Daughter'] = f_fnames[nIndex + 2]+ ' ' +s



        elif counter % 29 == 0 and nIndex + 3 <= len(m_fnames)-1 and nIndex + 3 <= len(f_fnames)-1:
            familyDict['Mother'] = f_fnames[nIndex]+ ' ' +s

            if counter % 2 == 0 and counter < 49:
                familyDict['Son'] = m_fnames[nIndex + 2]+ ' ' +s

            elif counter % 3 == 0 and counter < 49:
                familyDict['Daughter'] = f_fnames[nIndex + 2]+ ' ' +s

            else:
                familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s



        elif counter % 31 == 0 and nIndex + 3 <= len(m_fnames)-1 and nIndex + 3 <= len(f_fnames)-1:
            familyDict['Father'] = m_fnames[nIndex]+ ' ' +s

            if counter % 2 == 0 and counter < 49:
                familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s

            elif counter % 3 == 0 and counter < 49:
                familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s

            else:
                familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s



        elif counter % 37 == 0:
            familyDict['Mother'] = f_fnames[nIndex] + ' ' + s
            familyDict['Mother2'] = f_fnames[nIndex - 5] + ' ' + s

            if counter % 2 == 0 and counter < 49:
                familyDict['Son'] = m_fnames[nIndex + 2]+ ' ' +s

            elif counter % 3 == 0 and counter < 49:
                familyDict['Daughter'] = f_fnames[nIndex + 2]+ ' ' +s

            elif nIndex < 49:
                if nIndex % 2:
                    familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s
                    familyDict['Daughter2'] = f_fnames[nIndex + 2] + ' ' + s

                if nIndex % 3:
                    familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                    familyDict['Son'] = m_fnames[nIndex + 2] + ' ' + s

                else:
                    familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                    familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s



        elif counter % 41 == 0:
            familyDict['Father'] = m_fnames[nIndex]+ ' ' +s
            familyDict['Father2'] = m_fnames[nIndex - 5]+ ' ' +s

            if counter % 3 == 0 and counter < 49:
                familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s

            elif counter % 2 == 0 and counter < 49:
                familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s

            elif nIndex < 49:
                if nIndex % 2:
                    familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s
                    familyDict['Daughter2'] = f_fnames[nIndex + 2] + ' ' + s

                if nIndex % 3:
                    familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                    familyDict['Son'] = m_fnames[nIndex + 2] + ' ' + s

                else:
                    familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s
                    familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s


        else:
            familyDict['Father'] = m_fnames[nIndex]+ ' ' +s
            familyDict['Mother'] = f_fnames[nIndex]+ ' ' +s

            if counter % 2 == 0 and counter < 49:
                familyDict['Son'] = m_fnames[nIndex + 1] + ' ' + s

            elif counter % 3 == 0 and counter < 49:
                familyDict['Daughter'] = f_fnames[nIndex + 1] + ' ' + s

            else:
                pass



        familyList.append(familyDict)
        counter = counter + 1
        if nIndex == 49:
            nIndex = 1
        else:
            nIndex = nIndex + 1


print(familyList)

with open('new_families.txt', 'w') as nf:
    nf.write(str(familyList))

