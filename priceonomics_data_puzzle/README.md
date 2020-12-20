# Priceonomics Data Puzzle
- [Priceonomics Data Puzzle](#priceonomics-data-puzzle)
  - [About](#about)
  - [Directory](#directory)
  - [Results](#results)
  - [Additional analysis](#additional-analysis)

---

## About
TreefortBnb, Airbnb's fictious rival, connects luxurious treefort homes around the United States. Priceonomics curated a dataset with the pricing of different treeforts and challenged us to find the median price of booking a treefort in each of the top 100 cities. Full backstory and challenge available [here](https://priceonomics.com/the-priceonomics-data-puzzle-treefortbnb/).

More specifically, Priceonomics requested us to:
- Send us back a table with a list of the median price in each city, ranked from most to least expensive.
- Restrict your analysis to just to the "top 100" cities that have the most units on the market.

<br>
<a href = "#priceonomics-data-puzzle"> :arrow_up: Table of Contents </a>
<br>
<br>

## Directory
This repository contains solutions to the Priceonomics Treefortbnb challenge in R and Python. Note: Python analysis in Jupyter Notebook and rendered to HTML for in-line analysis.
Solutions used the following steps.
1. Load libraries
2. Import data
3. Clean data
4. Conduct stated analysis
5. Additional EDA


<br>
<a href = "#priceonomics-data-puzzle"> :arrow_up: Table of Contents </a>
<br>
<br>

## Results
Median prices for the top 100 cities in the dataset are available in the *solution.csv*. 
Below are the top 10 results:

| Rank | city | state | median_price_USD
| :-- | :-- | :-- | --:
1 | Indianapolis | IN | 650
2 | Malibu | CA | 304
3 | Park City | UT | 299
4 | Truckee | NV | 275
5 | Healdsburg | CA | 275
6 | Laguna Beach | CA | 268.5
7 | Incline Village | NV | 259
8 | Manhattan Beach | CA | 209
9 | Charlotte | NC | 200
10 | Sonoma | CA | 200

<br>
<a href = "#priceonomics-data-puzzle"> :arrow_up: Table of Contents </a>
<br>
<br>


## Additional analysis
I was surprised that Indianapolis, IN topped the list. As a state capital, I expected it to be high, but not higher than a globally recognized city like San Francisco. However, I was interested that its median price is double that of the second highest city: Malibu, Ca. The median is a robust statistic that is not sensitive to outliers. I suspected that the data had a right skew and investigated.

To better understand the dataset, I plotted a histogram of the USD price for all units.

![](https://user-images.githubusercontent.com/50056791/87379074-3c663280-c544-11ea-9fce-fe0c8c77b46a.png)

*created in puzzle_solution.ipynb*

There are _many_ treeforts above $2,000! There are even some units listed for $10,000!

Next, I looked specifically at the listings for the most expensive median city in the US: Indianapolis, IN.
| Statistic | price_USD |
| :--       | --: |
| units   |  251   |
| mean   |  915.40 |
| st_dev | 969.65 |
| min | 33 |
| max | 5500 |
| Q1 | 162.5 |
| Q2 | 650 |
| Q3 | 1200 |

The mean price for a treefortBnb in Indianapolis is $915.40, with a standard deviation of 969.65, and a range from $33 - $5,500! There is something questionable about the data here - I can't imagine many people paying $5,500 for a treehouse!

Priceonomics also conveniently records the number of reviews for each treefort. Below is a scatterplot of each Indianapolis $ Price vs Number of Reviews.
![](https://user-images.githubusercontent.com/50056791/86996325-334e1d80-c160-11ea-851d-f29417e14f4d.png)

*created in puzzle_solution.R*

The graph shows that prices above $1,000 USD generally have 0 reviews.


If we consider reviews to be a proxy measure for visits, we can assume that these units do not constitute normal treefortBnb experiences. I suspected that this same relationship is present in the larger dataset and thus graphed a scatterplot of Unit Price USD vs Number of Reviews for all data.

![](https://user-images.githubusercontent.com/50056791/87259605-59760500-c461-11ea-8c22-59cd2c4e2248.png)

*created in puzzle_solution.ipynb*

Bingo! It appears that the more expensive the treefort is, the fewer reviews it has. The spirit of the median (and other measures of central tendency) is to get an understanding of _normal_ in the dataset. I doubt that a $10,000 treefort consistutes a 'normal' experience for renters.

To better represent normal, I re-calculated the median price of booking a treefort in each of the top 100 cities, given the records had 1+ reviews.
| city |	state | median_price_usd |	
| :-- | :-- | --: |
| Carmel |	CA |	300.0 |
| Malibu |	CA |	225.0 |
| Truckee |	NV |	200.0 |
| Laguna Beach |	CA |	200.0 |
| Incline Village |	NV |	200.0 |


Of course, it doesn't matter whether or not the listings had reviews --Treefort BnB is fictional and none of the records represent a _real_ experience. However, this is a useful exercise to demonstrate how a single (robust) measure of central tendency can tell a misleading story and you should always be ready to dig deeper into the data (:

<br>
<a href = "#priceonomics-data-puzzle"> :arrow_up: Table of Contents </a>
<br>
<br>