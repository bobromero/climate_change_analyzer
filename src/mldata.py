import pandas as pd
import os
#This file uses NaturalDisasters1900-2025WithCoords.csv data and 
#reduces the data used by the machine learning algorithm
def remove_unwanted_cols(fileName):
    fileName = fileName.drop(columns=["Historic"])
    fileName = fileName.drop(columns=["Classification Key"])
    fileName = fileName.drop(columns=["External IDs"])
    fileName = fileName.drop(columns=["Event Name"])
    fileName = fileName.drop(columns=["CPI"])
    fileName = fileName.drop(columns=["Unnamed: 0"])
    fileName = fileName.drop(columns=["DisNo."])
    fileName = fileName.drop(columns=["Associated Types"])
    fileName = fileName.drop(columns=["OFDA/BHA Response"])
    fileName = fileName.drop(columns=["Appeal"])
    fileName = fileName.drop(columns=["Declaration"])
    fileName = fileName.drop(columns=["AID Contribution ('000 US$)"])
    fileName = fileName.drop(columns=["River Basin"])
    fileName = fileName.drop(columns=["No. Injured"])
    fileName = fileName.drop(columns=["No. Affected"])
    fileName = fileName.drop(columns=["No. Homeless"])
    fileName = fileName.drop(columns=["Total Affected"])
    fileName = fileName.drop(columns=["Reconstruction Costs ('000 US$)"])
    fileName = fileName.drop(columns=["Reconstruction Costs, Adjusted ('000 US$)"])
    fileName = fileName.drop(columns=["Insured Damage ('000 US$)"])
    fileName = fileName.drop(columns=["Insured Damage, Adjusted ('000 US$)"])
    fileName = fileName.drop(columns=["Total Damage ('000 US$)"])
    fileName = fileName.drop(columns=["Total Damage, Adjusted ('000 US$)"])
    fileName = fileName.drop(columns=["Admin Units"])
    fileName = fileName.drop(columns=["Last Update"])
    fileName = fileName.drop(columns=["Entry Date"])
    fileName = fileName.drop(columns=["Origin"])


inputFilePath = "../data/NaturalDisasters1900-2025WithCoords.csv"

outputFilePath = "../data/NaturalDisastersOnly.csv"

df = pd.read_csv(inputFilePath)


#1) Only keeping natural disasters and wanted columns

naturalDisastersOnly = df[df["Disaster Group"]== "Natural"]
remove_unwanted_cols(naturalDisastersOnly)

#the ml algorithm target is magnitude so every row with an empty Magnitude
#column has to be eliminated:
naturalDisastersOnly = naturalDisastersOnly.dropna(subset=['Magnitude']) 
naturalDisastersOnly.to_csv(outputFilePath, index=False)
ofp = pd.read_csv(outputFilePath)

#2) Separating rows by Disaster Types

 #Earthquake
earthquakesOnlyFP = "../data/earthquakesOnlyFP.csv"
earthquakesOnly = ofp[ofp["Disaster Type"]=="Earthquake"]
earthquakesOnly.to_csv(earthquakesOnlyFP, index=False)
















