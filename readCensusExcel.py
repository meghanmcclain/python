#! python3

# readCensusExcel.py - Tabulates population & number of census tracts for
# each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
#empty dictionary
countyData = {}

# Fill in countyData with each county's population & tracts.
print('Reading rows...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exist.
    # if state key exists, parameter {} has no effect
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    # if county key doesn't exist in dict, the value becomes the key's value
    countyData[state].setdefault(county, {'tracts': 0, 'pop':0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file & write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')