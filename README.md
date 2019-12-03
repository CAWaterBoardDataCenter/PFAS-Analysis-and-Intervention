# PFAS-Analysis-and-Intervention

Analysis of PFAS contamination level data may be time consuming or the personnel to do the analysis is non-existent. With PFAS awareness and monitoring on the rise the goal of this project is to prepare testing organizations for further regulations, expedite the analysis process, as well as help to proactively implement interventions to prevent further contamination. The anticipated impacts would be to identify possible sources of contamination and stop the spread of PFAS at the source as well as implementing monitoring events.

The working app can be found here: https://meldataaa.shinyapps.io/PFAS_Analysis_and_Intervention/

Use Test Data.csv to see the visualizations currently being produced when a user uploads their data in the correct format.

### December 2, 2019

# Ideas for Further Improvement
Some of these are merely thoughts while some need minor code changes.

## Analysis
- Weather API implementation
  -	Given a user inputs a start and end date of their data and a lat/long of the test site location, pull historical weather data and plot variables such as rainfall.
  -	Historical weather data must be paid for on Googles OpenWeatherMap service as well as Dark Sky API
- Watershed
-	Add any other useful visualizations for chemical concentrations, weather, etc. 

## Possible Intervention
-	Zoom to Site Location as opposed to all of California
-	Filter list to show locations within a certain radius of the specified site location
-	Export list of facilities
-	Choose multiple facility types
- Add other location types
  -	Military Facilities
  -	Airports
  -	Firefighting Training Facilities
  -	EPA’s Superfund National Priorities List (NPL)
  -	US Toxic Release Inventory (TRI)
      https://toxmap.nlm.nih.gov/toxmap/app/
  - National Air Toxics Assessment
      https://www.epa.gov/national-air-toxics-assessment
      
## Information & Help
- Add links to important information
  -	RMP, potentially hazardous sites
      https://www.epa.gov/rmp
      https://www.epa.gov/rmp/list-regulated-substances-under-risk-management-plan-rmp-program
  - Landfills	
      https://www.epa.gov/lmop/landfill-technical-data
  - UCMR 3
      https://www.epa.gov/dwucmr/third-unregulated-contaminant-monitoring-rule
  - Evaluation of a national data set for insights into sources, composition, and concentrations of per- and polyfluoroalkyl substances    (PFASs) in U.S. drinking water
      https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5849529/
  - PFAS Laws & Regulations
      https://www.epa.gov/pfas/pfas-laws-and-regulations
  - Drinking Water Treatability Database
      https://oaspub.epa.gov/tdb/pages/contaminant/contaminantOverview.do?contaminantId=11020
  - Storm Water Events by Year Data
      https://www.ncdc.noaa.gov/stormevents/ftp.jsp
  - Multi-System Search
      https://enviro.epa.gov/facts/multisystem.html
      https://www.epa.gov/enviro/system-data-searches
      https://enviro.epa.gov/facts/tri/ef-facilities/#/Facility/91016MXXXX1601S
## Other
- Better format? Dashboard? Map with interactive layers?
- This application could easily be used for other contaminants as well, if the user's data is in the specified format.
- Open to all ideas and suggestions! 
