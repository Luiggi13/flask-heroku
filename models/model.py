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
        "bannerTemplateKey": 0,
    }
    return OBJ_BASE


def carList():
    CARSBASE = [
        {"name_car": "Aston Martin Racing V12 Vantage GT3", "id_car": 1},
        {"name_car": "Aston Martin Racing V8 Vantage GT3", "id_car": 2},
        {"name_car": "Audi R8 LMS", "id_car": 3},
        {"name_car": "Audi R8 LMS Evo", "id_car": 4},
        {"name_car": "Bentley Continental GT3 2015", "id_car": 5},
        {"name_car": "Bentley Continental GT3 2018", "id_car": 6},
        {"name_car": "Bentley Continental GT3", "id_car": 7},
        {"name_car": "BMW M6 GT3", "id_car": 8},
        {"name_car": "Emil Frey Jaguar GT3", "id_car": 9},
        {"name_car": "Ferrari 488 GT3", "id_car": 10},
        {"name_car": "Ferrari 488 GT3 2018", "id_car": 11},
        {"name_car": "Ferrari 488 GT3 Evo", "id_car": 12},
        {"name_car": "Honda NSX GT3", "id_car": 13},
        {"name_car": "Honda NSX GT3 Evo", "id_car": 14},
        {"name_car": "Lamborghini Huracan GT3", "id_car": 15},
        {"name_car": "Lamborghini Huracan GT3 Evo", "id_car": 16},
        {"name_car": "Lamborghini Huracan GT3", "id_car": 17},
        {"name_car": "Lamborghini Huracan ST", "id_car": 18},
        {"name_car": "Lexus RC F GT3", "id_car": 19},
        {"name_car": "McLaren 650S GT3", "id_car": 20},
        {"name_car": "McLaren 720S GT3", "id_car": 21},
        {"name_car": "Mercedes-AMG GT3", "id_car": 22},
        {"name_car": "Mercedes AMG GT3 2015", "id_car": 23},
        {"name_car": "Mercedes AMG GT3 Evo", "id_car": 24},
        {"name_car": "Nissan GT-R Nismo GT3 2015", "id_car": 25},
        {"name_car": "Nissan GT-R Nismo GT3 2018", "id_car": 26},
        {"name_car": "Nissan GT-R Nismo GT3", "id_car": 27},
        {"name_car": "Porsche 991 GT3 R", "id_car": 28},
        {"name_car": "Porsche 991 II GT3 Cup", "id_car": 29},
        {"name_car": "Porsche 991 II GT3 R", "id_car": 30},
        {"name_car": "Reiter Engineering R-EX GT3", "id_car": 31},
    ]
    return CARSBASE


def carNotFound():
    NOTFOUNDCAR = {"error": "There aren't any car with this id"}
    return NOTFOUNDCAR
