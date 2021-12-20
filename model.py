def baseJson():
  OBJ_BASE = {
    "carGuid": 0,
    "teamGuid": 0,
    "raceNumber": 55,
    "raceNumberPadding": 0,
    "auxLightKey": 1,
    "auxLightColor": 524,
    "skinTemplateKey": 99,
    "skinColor1Id": 354,
    "skinColor2Id": 345,
    "skinColor3Id": 524,
    "sponsorId": 0,
    "skinMaterialType1": 1,
    "skinMaterialType2": 1,
    "skinMaterialType3": 1,
    "rimColor1Id": 1,
    "rimColor2Id": 345,
    "rimMaterialType1": 2,
    "rimMaterialType2": 1,
    "teamName": "Arrincadeira Team Cup",
    "nationality": 0,
    "displayName": "Martin Trasancos",
    "competitorName": "",
    "competitorNationality": 0,
    "teamTemplateKey": 0,
    "carModelType": 9,
    "cupCategory": 0,
    "licenseType": 0,
    "useEnduranceKit": 1,
    "customSkinName": "Arrincadeira Team Cup",
    "bannerTemplateKey": 0
  }
  return OBJ_BASE

def carList():
  CARSBASE = [
    {
      "id_car" :1,
      "name_car": "BMW M6 GT3"
    }
  ]
  return CARSBASE

def carNotFound():
  NOTFOUNDCAR = {
      "error": "There aren\'t any car with this id"
    }
  return NOTFOUNDCAR