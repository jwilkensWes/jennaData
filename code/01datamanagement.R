## data management

# packages
library(tidyverse)
library(readxl)
library(qacBase)

# data
updated_master_wEVT_030323 <- read_excel("data/rawdata/updated.master.wEVT.030323.xlsx")
evt <- updated_master_wEVT_030323
igndates <- read_csv("data/rawdata/ignitions one.csv")

# select only necessary columns
firepoints <- evt %>%
  select(OBJECTID, Fire, Category, POINT_X, POINT_Y)
glimpse(firepoints)

# get wanted fires
fires <- evt %>% 
  select(Fire)
fires <- distinct(fires)

summary(igndates)
igndates <- igndates %>% 
  select(`Fire Name`, `Ignition Date`, `Fire ID`)
igndates <- na.omit(igndates)
glimpse(igndates)

# rename vars and turn vars to lowercase 
names(firepoints) <- tolower(names(firepoints))
firepoints

fires$fire <- factor(fires$Fire)
fires$Fire <- NULL

igndates$firename <- igndates$`Fire Name`
igndates$`Fire Name` <- NULL
igndates$ignitiondate <- igndates$`Ignition Date`
igndates$`Ignition Date` <- NULL
igndates$fireID <- igndates$`Fire ID`
igndates$`Fire ID` <- NULL


# make all firenames lowercase
igndates$firename <- tolower(igndates$firename)
fires$fire <- tolower(fires$fire)
firepoints$fire <- tolower(firepoints$fire)
firepoints$category <- tolower(firepoints$category)


# edit fire names
igndates[109, 1] <- "wood springs2"
igndates[115, 1] <- "basin 5102020"
igndates[37, 1] <- "blue river 662020"

# join datasets together
fire_ign <- firepoints %>% 
  left_join(igndates, by = c("fire" = "firename"))

summary(fire_ign)
contents(fire_ign)

# get 3 month period before
fire_ign$ignitiondate <- mdy(fire_ign$ignitiondate)
fire_ign <- fire_ign %>% 
  mutate(prior3m_ign = ignitiondate %m-%months(3))




# save dataset
save(fire_ign, file = "data/cleandata/fire_ign.Rda")
write.csv(fire_ign, file = "data/cleandata/fire_ign.csv", row.names = FALSE)
