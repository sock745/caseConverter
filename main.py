def convertToSnakeCase(pascalCamelCasedString):
  snakeCaseList = []
  for char in pascalCamelCasedString:
    if char.isupper():
      convertedCharacter = '_' + char.lower()
      snakeCaseList.append(convertedCharacter)
    else:
      snakeCaseList.append(char)
      pass
