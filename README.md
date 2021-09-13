# **PyBer Rideshare Analysis**

## **Overview**
> PyBer is a ride-sharing app that has asked us to perform an analysis on some data. By using `Pandas` and `Matplotlib`, we must create a summary DataFrame of the [ride-sharing data](https://github.com/annaS000/Rideshare-Analysis/tree/main/Resources) and a multiple-line graph that shows the total weekly fares for each city type. After collecting our results, we must provide written report that summarizes the differences in our findings by city type and ultimately give business reccomendations for PyBer.

---

## **Code**
[Link](https://github.com/annaS000/Rideshare-Analysis/blob/main/PyBer_Challenge.ipynb) to Python code used to perform analysis.

> All of my functions and dependencies used are stored in the file [anna.py](https://github.com/annaS000/Rideshare-Analysis/blob/main/anna.py)

---

## **Results**
### **PyBer Fare Summary**
![ride date](https://raw.githubusercontent.com/annaS000/Rideshare-Analysis/main/Resources/ride_data_by_city_type.png)
> Here we can see the differences in ride-sharing data for Rural, Suburban, and Urban areas. **Urban areas** have the most rides, drivers, and the lowest rates for ride fares. **Rural areas** have the least amount of rides and drivers and the most expensive ride fares.  **Suburban areas** don't have as many rides or drivers as Urban places but are more successful than Rural places. and has the mid-range price out of the three types for ride fares. In regards to the **Total Fares**, Urban cities received about double the amount of fares compared to Suburban cities and almost 10 times more than Rural cities.


### **Multiple-line Chart of Total Fare by City Type**
![data by week](https://raw.githubusercontent.com/annaS000/Rideshare-Analysis/main/analysis/PyBer_fare_summary.png)
> This line graph displays the total fares per week for each city between the months of January and April. **Urban areas** saw highs and lows in Total Fares during the month of March. **Suburban** and **Rural areas** did not experience many changes throughout the given months except for a few subtle peaks and dips. We can see all city types had a spike in Total Fare towards the end of February.

### **A Closer Look at February**
![times for feb](https://raw.githubusercontent.com/annaS000/Rideshare-Analysis/main/analysis/Feb_summary.png)
> To investigate the shared peak in February, I created another chart to see what specific days had more activity. Here, we can see that around February 17th-19th there were higher totals in fares, most prominently affecting the numbers for Suburban and Urban cities. In 2019, February 18th was the third Monday which is President's Day. Since it was a holiday, more people may have had off from work or school. This could have allowed them to be able to travel on those days, which can explain the increase in total fares during that time.


---

## **Summary**

### **Conclusions and Recommendations**
After reviewing the information that was extracted from the ride-sharing data, a few things can be considered:
1. **Urban areas** are, usually, densely populated so the demand for public transportation is higher than other areas which explains the difference in numbers of drivers/rides and total fare compared to the Suburbs and Rural cities. **Suburban areas** had less rides and drivers than Urban areas but also more than Rural areas. These areas may have more schools and 9-5 jobs which means they can be more affected by federal holidays such as President's Day. Taking note of holidays can be beneficial to the company because these will be days more people are expected to travel. Perhaps there can be sales or promotions on these days to get more people to use the service.
    <br/>

2. **Rural areas** had less rides and drivers with higher fares to make up for the lack of demand in this service. This makes sense because Rural areas have more spread out land and more people most likely own their own vehicles. Additionally, something that is a hurdle for rural areas is internet access. According to an article from [Vox](https://www.vox.com/the-goods/2019/1/11/18179036/uber-lyft-rural-areas-subscription-model) on Uber and Lyft, apps similar to PyBer, "Technological infrastructure is one of the biggest challenges in rural areas. Uber and Lyft both depend on good cell service, something that can be spotty in small towns." This deters these areas from using apps like PyBer. Later in the article, it discusses a study that assigned ride-sharing indexes using median income, population density, unemployment, and licensed drivers to counties in Pennsylvania. This was used to determine whether or not certain rural areas could benefit from ride-hailing apps. It was concluded that "all these variables are high, a country is more likely to embrace ride-hailing." With this information, PyBer can take those factors into consideration and can focus on expanding their services in Rural areas that are most compatible.
    <br/>

3. Overall, it can be beneficial for the company to take a closer look at this data as well as analyzing data of other years as well to confirm if these findings are reoccuring trends. Another interesting variable that can be analyzed is the change in activity depending on the time of day. We could also compare activity of different days of the week. For example, one hypothesis to investigate could be weekends may have more ride requests than week days because there is more free time to travel and go out. To piggyback off that idea, collecting data on the number of bars or airports in a city could be information of interest as they are places that people need rides to and from.

---

## **References**

[Click to view citation](https://github.com/annaS000/Rideshare-Analysis/blob/main/PyBer_References.pdf)