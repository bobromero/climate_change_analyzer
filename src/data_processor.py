import pandas as pd


def getData(file_name):
    df = pd.read_csv(file_name, encoding="ISO-8859-1")
    return df


def checkCoords(df):
    pairCount = 0
    onlyLong = 0
    onlyLat = 0
    nothing = 0
    # 26918 entries
    # Longitude 24
    # Latitude 23
    # we expect len(df)
    for item in df.iterrows():
        # print(row[1]['Latitude'])
        row = item[1]
        lonExist = row["Longitude"] > 0
        latExist = row["Latitude"] > 0
        if lonExist and latExist:
            pairCount += 1
        elif lonExist:
            onlyLong += 1
        elif latExist:
            onlyLat += 1
        else:
            nothing += 1
    pairs = ("Pairs:", pairCount)
    longs = ("Only Long", onlyLong)
    lats = ("Only Lat", onlyLat)
    none = ("Nothing", nothing)
    return (pairs, longs, lats, none)


def getCountry(countrydf, country):
    for citem in countrydf.iterrows():
        crow = citem[1]

        # politics
        if country == "Taiwan (Province of China)":
            country = "Taiwan"
        if country == "United States of America":
            country = "United States"
        if country == "Türkiye":
            country = "Turkey"
        if country == "Cabo Verde":
            country = "Cape Verde"
        if country == "Myanmar":
            country = "Myanmar [Burma]"
        if country == "China, Hong Kong Special Administrative Region":
            country = "China"
        if country == "United Kingdom of Great Britain and Northern Ireland":
            country = "United Kingdom"
        if country == "Soviet Union":
            country = "Russia"
        if country == "Netherlands (Kingdom of the)":
            country = "Netherlands"
        if country == "Germany Federal Republic":
            country = "Germany"
        if country == "Czechoslovakia":
            country = "Czech Republic"
        if country == "Republic of Korea":
            country = "South Korea"
        if country == "Bolivia (Plurinational State of)":
            country = "Bolivia"
        if country == "Venezuela (Bolivarian Republic of)":
            country = "Venezuela"
        if country == "Azores Islands":
            return (37.7412, 25.6756)
        if country == "Iran (Islamic Republic of)":
            country = "Iran"
        if country == "Democratic Republic of the Congo":
            country = "Congo [DRC]"
        if country == "Congo":
            country = "Congo [Republic]"
        if country == "German Democratic Republic":
            return (52.434, 12.5145)
        if country == "Viet Nam":
            country = "Vietnam"
        if country == "Canary Islands":
            return (28.2916, 16.6291)
        if country == "United Republic of Tanzania":
            country = "Tanzania"
        if country == "Yugoslavia":
            return (43.9159, 17.6791)
        if country == "Wallis and Futuna Islands":
            return (14.2938, 178.1165)
        if country == "Syrian Arab Republic":
            country = "Syria"
        if country == "Lao People's Democratic Republic":
            country = "Laos"
        if country == "Yemen Arab Republic":
            country = "Yemen"
        if country == "Russian Federation":
            country = "Russia"
        if country == "Micronesia (Federated States of)":
            country = "Micronesia"
        if country == "Czechia":
            country = "Czech Republic"
        if country == "South Sudan":
            country = "Sudan"
        if country == "Eswatini":
            country = "Swaziland"
        if country == "Sao Tome and Principe":
            country = "São Tomé and Príncipe"
        if country == "North Macedonia":
            country = "Macedonia [FYROM]"
        if country == "Democratic People's Republic of Korea":
            country = "North Korea"
        if country == "Republic of Moldova":
            country = "Moldova"
        if country == "State of Palestine":
            return (31.9522, 35.2332)
        if country == "China, Macao Special Administrative Region":
            country = "China"
        if country == "People's Democratic Republic of Yemen":
            country = "Yemen"
        if country == "Serbia Montenegro":
            country = "Montenegro"
        if country == "Brunei Darussalam":
            country = "Brunei"
        if country == "Curaçao":
            return (12.1696, 68.9900)
        if country == "United States Virgin Islands":
            country = "U.S. Virgin Islands"
        if country == "Saint Barthélemy":
            return (17.9000, 62.8333)
        if country == "Saint Martin (French Part)":
            return (18.0826, 63.0523)
        if country == "Sint Maarten (Dutch part)":
            return (18.0425, 63.0548)

        binaryrep = " ".join(format(ord(x), "b") for x in country)
        # Côte dIvoire
        if (
            binaryrep
            == "1000011 11110100 1110100 1100101 100000 1100100 10010010 1001001 1110110 1101111 1101001 1110010 1100101"
        ):
            country = "Côte d'Ivoire"

        if crow["name"] == country:
            # print("found ", country)
            return (crow["latitude"], crow["longitude"])

    print("couldn't find ", country)
    return (0, 0)


def updateCoords(df):
    countrydf = getData("../data/CountryData.csv")

    for item in df.iterrows():
        row = item[1]
        lonExist = row["Longitude"] > 0
        latExist = row["Latitude"] > 0

        country = row["Country"]

        if lonExist and latExist:
            continue
        elif lonExist:
            # get the lat of the country
            coords = getCountry(countrydf, country)
            df.loc[item[0], "Latitude"] = coords[0]
        elif latExist:
            # get the long onf the country
            coords = getCountry(countrydf, country)
            df.loc[item[0], "Longitude"] = coords[1]
        else:
            # get the coords of the country
            coords = getCountry(countrydf, country)
            df.loc[item[0], "Latitude"] = coords[0]
            df.loc[item[0], "Longitude"] = coords[1]

    df.to_csv("../data/NaturalDisasters1900-2025WithCoords.csv")
    return df


def load_disaster(type, cols=None):
    if cols is None:
        cols = []
    df = pd.read_csv("../data/NaturalDisasters1900-2025WithCoords.csv")
    df = df[df["Disaster Type"] == type]
    new_df = df[cols]
    return new_df


def describe_data():
    df = pd.read_csv("../data/NaturalDisasters1900-2025WithCoords.csv")
    print(df.describe())


if __name__ == "__main__":
    # anything that is not a function will be here
    file_name = "../data/NaturalDisasters1900-2025.csv"

    menu = f"""
    Data Processor - raw file - {file_name} 
    1. List data
    2. Show data columns
    3. Check how many entries have coordinates
    4. 

    """
    df = getData(file_name)

    cdf = getData("../data/NaturalDisasters1900-2025WithCoords.csv")
    # updateCoords(df,False)
    # while True:
    #
    #     print(menu)
    #

    print(f"Before {checkCoords(df)}")
    print(f"After {checkCoords(cdf)}")
