
# Author Info -------------------------------------------------------------
"
Author: Jai Miles
Date: 07/01/2020
Purpose: Priceonomics Puzzle
Source: https://priceonomics.com/the-priceonomics-data-puzzle-treefortbnb/


Challenge: Tell us the median price of booking a room in each of the top 100 cities in this data set. 


Stated Considerations:
- More specifically, send us back a table with a list of the median price in each city, ranked from most to least expensive. 
- Restrict your analysis to just to the \"top 100\" cities that have the most units on the market.


Extra Considerations:
- There may be duplicate city names in different states. 
  I will handle this by first grouping cities & states and then counting cities.
  NOTE: Some of these duplicates may be from data entry, e.g., Berkeley, CO is a city neighborhood.

- Don't assume that all data has uniform input.
  After working with the data, I discovered case inconsistencies, 
  e.g., New York, NY vs new york, NY. In analysis, I considered these the same cities.

- Some locations may be listed under different names. 
  After grouping the data, I noticed that Miami and Miami beach are both listed. 
  With some research, I decided to group the two separately.
  https://www.tripadvisor.com/ShowTopic-g34438-i92-k1409657-Whats_the_difference_between_miami_and_miami_beach-Miami_Florida.html
"




# Libraries & packages ----------------------------------------------------
"
Section Steps
1. Install libraries
2. Load libraries

dplyr - data manipulation and analysis.
purr - data validation and extra analysis at end.
huxtable - pretty printing results to console.
ggplot2 - additional data exploration.
"


##########
# Install
##########
## Uncomment below to install

packages = c(
  "dplyr",
  "purrr",
  "huxtable",
  "ggplot2"
)

# for (p in packages) {
#   if (!require(p, character.only = T)) {
#     install.packages(p)
#   }
# }


##########
# Load
##########

for (p in packages) {
  library(p, character.only = T)
}



# Import & clean data -----------------------------------------------------
"
Section Steps
1. Import data
2. Clean column names
3. Check for missing values
4. Check all data is correct type
5. Clean string data
"


##########
# Import data
##########

filename_weburl = "https://pix-media.priceonomics-media.com/Data+for+TreefortBnB+Puzzle.csv"

data_treefortbnb <- read.csv( filename_weburl,
                              header = TRUE,
                              sep = ",",
                              strip.white = TRUE
)
View(data_treefortbnb)


##########
# Clean Column names
##########

colnames(data_treefortbnb)

new_col_names <- c(
  "id",
  "city",
  "state",
  "price_USD",
  "num_reviews"
)
colnames(data_treefortbnb) <- new_col_names
colnames(data_treefortbnb)


##########
# Check missing values
##########

colSums( is.na(data_treefortbnb))   # No N/As to handle


##########
# Check data frame types
##########

## Check type of each column
is_integer(data_treefortbnb$id)
is_character(data_treefortbnb$city)
is_character(data_treefortbnb$state)
is_numeric(data_treefortbnb$price_USD)
is_integer(data_treefortbnb$num_reviews)

"
NOTE:
city & state yield false for is_character test. This behavior can be inconsistent, so investigate.
"

typeof(data_treefortbnb$city)
typeof(data_treefortbnb$state)

sort(unique(data_treefortbnb$city))   ## Note: not uniform case across city names
sort(unique(data_treefortbnb$state))

"
Strings were automatically converted to factors, which are built ontop of the integer class.

Also, need to transform factors to lowercase for consistency, e.g., new york, NY vs New York, NY.
"


##########
# Clean string data
##########

## Make all cities & states lowercase for grouping.
data_treefortbnb$city <- tolower(data_treefortbnb$city)
data_treefortbnb$state <- tolower(data_treefortbnb$state)
View(data_treefortbnb)

sort(unique(data_treefortbnb$city))
sort(unique(data_treefortbnb$state))
"
Fixed issues with different city cases.
"




# Analysis ----------------------------------------------------------------
"
Section Steps
1. Count duplicate city names
2. Find top 100 cities with most units on market
3. Sort by price, units
4. Format data (USD Format, case, remove units and reviews)
"


##########
# Count duplicates
##########

## Group by city & state, then summarise

unique_city_states <- data_treefortbnb %>% 
  group_by( city, state) %>% 
  summarise()

unique_city_states


## Count duplicate states
sum( duplicated( unique_city_states$city))

"
Found that there are 22 cities with the same name, e.g., Berkeley CA & Berkeley CO.
This is good to know, but overlapping city names are already handled by group_by(city, state)
"


##########
# Top 100 cities with most units on market. 
##########
"
Group by city and state
then count units and calc med
then arrange by units.
"

median_cost_per_city <- data_treefortbnb %>%
  group_by( city, state) %>%
  summarise(
    units = n(),
    median_price_USD = median(price_USD),
    total_reviews = sum(num_reviews)
  ) %>% 
  arrange( desc(units))

View(median_cost_per_city)


# Quick data check that same number of units and reviews as initial dataset
sum(median_cost_per_city$units) == nrow(data_treefortbnb)
sum(median_cost_per_city$total_reviews) == sum(data_treefortbnb$num_reviews)


## Take top 100 cities on market
top_100_cities <- head(median_cost_per_city, 100)
View(top_100_cities)


##########
# Sort by price, units
##########
"
Sorts by descending for median_price_USD and then units.
"
top_100_cities_by_price <- top_100_cities[order(-top_100_cities$median_price_USD, - top_100_cities$units),]
View(top_100_cities_by_price)


##########
# Format data
##########
"
Change median_price_USD to 2 decimal format
Uppercase states
Title case cities
Remove unit column -- excess information not requested
"

## USD Format
top_100_cities_by_price$median_price_USD <- format( 
  round( top_100_cities_by_price$median_price_USD, 2), 
  nsmall = 2)
View(top_100_cities_by_price)


## Upper case states
top_100_cities_by_price$state <- toupper(top_100_cities_by_price$state)


## Capitalize each word in cities

# function to capitalize each word.
capwords <- function(s, strict = FALSE) {
  cap <- function(s) paste(toupper(substring(s, 1, 1)),
                           {s <- substring(s, 2); if(strict) tolower(s) else s},
                           sep = "", collapse = " " )
  sapply(strsplit(s, split = " "), cap, USE.NAMES = !is.null(names(s)))
}


top_100_cities_by_price$city <- capwords(top_100_cities_by_price$city)

View(top_100_cities_by_price)


## Remove units & total_reviews column

top_100_cities_by_price$units <- NULL
top_100_cities_by_price$total_reviews <- NULL
View(top_100_cities_by_price)




# Export data -------------------------------------------------------------
"
Section Steps
1. Pretty print table to console
2. Export table to csv
"

##########
# Pretty Print to console
##########

hux_top_100_cities_by_price <- 
  hux(top_100_cities_by_price) %>% 
  theme_basic() %>% 
  set_tb_padding(4)

print_screen(hux_top_100_cities_by_price,
             colnames = FALSE)


##########
# Export table
##########

solution_file_name = "Miles_Jai_Priceonomics_Puzzle_Solution.csv"

write.csv(top_100_cities_by_price,
          file = solution_file_name
          )




# Additional Analysis -----------------------------------------------------

##########
# Indianapolis, IN
##########
"
I did not expect Indianapolis, IN to have the highest median price.
I expected it to be high, but I consider it curious that it ranks higher than  
more populous, globally recognized cities like Los Angeles, and New York.
This is where specific domain knowledge, e.g., about the housing market, would 
be useful to understand the data.

Because the median is a robust statistic, the calculated unit price for Indianapolis, IN 
is not affected by outliers. I would be interested to closer inspect the city's data quartiles.
It is possible that the data follows a bimodal distribution, and there are more rentals offered 
in the higher pricing cluster. This would explain a higher median.
"
data_indianapolis_in <- data_treefortbnb %>% 
  filter(state == "in", city == "indianapolis")

View(data_indianapolis_in)

data_indianapolis_in %>% 
  summarise(
    num_units = n(),
    mean_cost = mean(price_USD),
    st_dev = sd(price_USD),
    min_price = min(price_USD),
    max_price = max(price_USD)
  )

"Note: slight difficulties with quantiles in dplyr. Need to pre-define quantiles, names, and functions before running."
percents <- c(0.25, 0.5, 0.75)    # define quantiles of interest
perc_names <- map_chr(percents, ~paste0(.x * 100, "%"))   # Create quantile names.
p_funcs <- map(percents, ~ partial(quantile, probs = .x, na.rm = TRUE)) %>% 
  set_names(nm = perc_names)
p_funcs


data_indianapolis_in %>% 
  summarise_at(
    vars(price_USD), funs(!!!p_funcs)
  )


"
Wow! Maximum price of $5,500 and q3 at $1,200. Something is definitely happening with the
treehouse market in Indianapolis.
"

ggplot(data = data_indianapolis_in, mapping = aes(x = price_USD)) + 
  geom_boxplot()


"
There are quite a few outliers past 2,000 USD.
The spirit of a central measure (median above) is to get something normal. 
With 251 observations, I still would not call anything in excess of $2,000 normal.

Let's plot this data vs the number of reviews.
"
colnames(data_indianapolis_in)
ggplot(data = data_indianapolis_in, 
       mapping = aes(x = price_USD, y = num_reviews)
       ) + 
  geom_point() +
  geom_smooth() +
  ggtitle("Price vs num reviews in Indianapolis, IN")

"
The graph shows that prices above $1,000 USD have 0 reviews.
If we consider reviews to be a proxy variable for visits, we can assume that these
units do not constitute normal treefortBnb experiences.
"



##########
# Investigate cities outside top 100
##########

lower_median_cost_per_city <- tail(median_cost_per_city, 24)
View(lower_median_cost_per_city)
"
Looking at the  median cost per city outside of the top 100, there are 12 cities with a 
single unit available. Many of these cities with a single unit have no reviews, 
while 3/4 of the cities with 2 units have 10+ reviews.

Many of these cities are duplicate names, e.g., Berkeley, CO. 
Upon further investigation, I discovered that Berkeley is a neighborhood city in Denver.
https://en.wikipedia.org/wiki/Berkeley,_Denver

I would be interested in double checking these low-entry units for clerical errors.
In the case of Berkeley, CO, this may reflect the data entry system and the correct
city is Berkeley, CA.
"

