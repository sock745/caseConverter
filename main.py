def convertToSnakeCase(pascalCamelCasedString):
  snakeCaseList = []
  for char in pascalCamelCasedString:
    if char.isupper():
      convertedCharacter = '_' + char.lower()
      snakeCaseList.append(convertedCharacter)
    else:
      snakeCaseList.append(char)
  snakeCasedString = ''.join(snakeCaseList)
  cleanSnakeCasedString = snakeCasedString.strip('_')
  return cleanSnakeCasedString
  snakeCaseList = ['_' + char.lower() if char.isupper() else char for char in pascalCamelCasedString]
  return ''.join(snakeCaseList).strip('_')

def main():
  print(convertToSnakeCase("oldMcdonaldHadAFarm")
  return

main()
