# NutriTable CREAtion: Analyze Diets with Italian CREA Food Tables

NutriTable CREAtion is a free open-source nutritional data calculator tool that helps researchers and clinicians to analyze the nutritional content of Italian meals based on data from the [Italian Council for Agricultural Research and Analysis of Agricultural Economic food tables](https://www.alimentinutrizione.it/sezioni/tabelle-nutrizionali). This tool allows users to select foods from a comprehensive list of 900 foods provided by [CREA](https://www.crea.gov.it/en/home), specify the quantity in grams, and get detailed information about the macro and micronutrients present in their selection.

<div align=center>
  <img src="https://github.com/FabbriniMarco/NutriTable-CREAtion/assets/83694005/b1adb2c3-c94e-4f59-9e17-893b080c6c71" width="650" height="420">
</div>

<br>
<br>

## Table of Contents

- [Features](#features)
- [Installation and usage](#installation-and-usage)
- [Add food and export data](#add-food-and-export-data)
- [Data Sources](#data-sources)
- [Acknowledgements](#acknowledgements)
- [Citation](#citation)
  
<br>
<br>

## Features

- **Extensive Food Database**: Includes nutritional data for 900 foods from the Italian CREA database. <br>
- **Detailed Nutritional Information**: Provides information on both macro and micronutrients for selected foods. <br>
- **Search Functionality**: Allows users to search for foods by name. <br>
- **Quantity Specification**: Users can specify the quantity of each food item to get proportionate nutritional information. <br>
- **Data Export**: Users can export the aggregated nutritional data to a TSV file. It's up to user choice wether to generate an export per-meal, per-daily intake or whatever time span. <br>
- **Clear Data**: Option to clear all inputs and start a new analysis. <br>
- **Info and Help Links**: Provides links to usage instructions and the original CREA database. <br>

For the moment the food data and tables encompass only italian terms. In a future release translation in English language will be made available.

<br>
<br>

## Installation and usage

### Windows user: portable pre-built .exe file
If you are a Windows user, you just need to fetch the NutriTableCREAtion.exe file either cloning this repo or downloading from the [Release](https://github.com/FabbriniMarco/NutriTable-CREAtion/releases) section.
Once downloaded simply double-click the .exe file. That's it!
<br>

### Linux user: run the python script
#### Prerequisites
- Python 3.7 or higher
- `ttkbootstrap` library
- `tkinter` library (usually comes pre-installed with Python)

Use pip to install the required libraries:
```sh
py -m pip install tk
py -m pip install ttkbootstrap
```

Clone this repository and navigate to the project directory:

```sh
git clone https://github.com/FabbriniMarco/NutriTable-CREAtion.git
cd NutriTable-CREAtion
python NutriTable-CREAtion.py
```

<br>
<br>

## Add food and export data

Select Food: Use the dropdown menu to select a food item. You can also search for a food by typing part of its name in the search bar. <br>
Enter Quantity: Enter the quantity (in grams) of the selected food. <br>
Add Food: Click the "Add Food" button to add the food to your list. The added foods along with their quantities will be displayed in a list. <br>
Export Data: Once done adding all the foods, click the "Export Data" button to save the nutritional information to a TSV file. <br>
Wipe Data: Click the "Wipe Data" button to clear all inputs and start a new analysis. You will be prompted to confirm this action. <br>
<br>

Info: Click the "Info" button for details about the program, including version, maintainer contact, and useful links. <br>
External Links: Use the "Github" and "CREA database" buttons to visit this project's GitHub repository and the original CREA database website, respectively. <br>

<br>
<br>

## Data Sources
The nutritional data used by this tool is sourced from the Italian Council for Agricultural Research and Analysis of Agricultural Economics (CREA) database. You can freely consult the CREA database here: https://www.alimentinutrizione.it/tabelle-nutrizionali/ricerca-per-ordine-alfabetico

<br>
<br>

## Acknowledgements
We thank the Italian Council for Agricultural Research and Analysis of Agricultural Economics (CREA) for their efforts in profiling foods and making the data publicly available.
You can check the list of contributors to the database creation at [this link](https://www.alimentinutrizione.it/gruppo-di-lavoro) and the bibliography behind the food tables data [here](https://www.alimentinutrizione.it/bibliografia).

<br>
<br>

## Citation
If you use this tool, please cite both the tool and the CREA database. 

```diff
@Manual{,
  title = {NutriTable-CREAtion: Analyze Diets with Italian CREA Food Tables},
  author = {Marco Fabbrini},
  year = {2024},
  note = {Version v1.0},
  url = {https://github.com/FabbriniMarco/NutriTable-CREAtion.git},
}
```
``` diff
@Manual{,
  title = {TABELLE DI COMPOSIZIONE DEGLI ALIMENTI, CREA AN, Aggiornamento 2019},
  author = {CREA-AN},
  year = {2019},
  url = {https://www.alimentinutrizione.it/tabelle-di-composizione-degli-alimenti},
}
```

Example: 
> Fabbrini, M. (2024) 'NutriTable-CREAtion: Analyze Diets with Italian CREA Food Tables'. Available on Github: https://github.com/FabbriniMarco/NutriTable-CREAtion.git
<br>

> CREA-AN (2019) 'TABELLE DI COMPOSIZIONE DEGLI ALIMENTI, CREA AN, Aggiornamento 2019'. Website: https://www.alimentinutrizione.it/tabelle-di-composizione-degli-alimenti
