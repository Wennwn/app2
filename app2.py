# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:56:11 2024

@author: Wendy
"""
import pandas as pd
import geopandas as gpd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.graph_objects as go
import plotly.offline as pyo


#structure 
st.title("Welcome to my datastory")
st.markdown("<b>A datastory by Wendy Willemsen | Big Data & Design | Hogeschool Utrecht </b>", unsafe_allow_html=True)
st.markdown("<b> Date: March 14th 2024 </b>", unsafe_allow_html=True)

# Adding an image to the introduction
image_path = r"C:\Users\Wendy\OneDrive\Afbeeldingen\Schermopnamen\money.jpg"
st.image(image_path, use_column_width=True)

#Some text to structure the dashboard
st.text("In this datastory we will dive into inflation, income and happiness scale.")
st.text("With this data we will dive into the endless controversy,")
st.text("of the discussion on how richness equals happiness.")
st.write("---")
st.title("Introduction")
st.text("For this datastory I use three different datasets from Kaggle.The first one is")
st.text("a Happiness index from the years 2015 - 2022, the second one about global")
st.text("inflation monitored from 2015 till 2024, and the third one is zooming in") 
st.text("on income and unemployment of OECD & OPEC countries.")
st.write("---")

#Streamlit layout
st.title("Global Happiness Score")
st.markdown("<b> A The Happiness score is reported by the World Happiness Report.</b>", unsafe_allow_html=True)
# Adding an image to the introduction
image_path = r"C:\Users\Wendy\Downloads\happiness-index-domains.png"
st.image(image_path, use_column_width=True)

#Legend/layout.
st.text("The score, going from 1 to 10 is based on answers to the")
st.text("main life evaluation question.")
st.write("---")
st.text("Important: To understand the mean in this dataset, note te following:")
st.text("The happiness score is monitored from 2015 to 2022.In this vizualtion we") 
st.text("used the mean of these years. This is because the difference per year is")
st.text("mostly only 1 or 2 decimal points.")
#_____________________________________________________________________________
#Importing data of happiness
happiness_score = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\Final_Happiness_Score.csv")

# List of columns to keep
columns_to_keep = ["Country","Happiness Score_2015", "Happiness Score_2016", "Happiness Score_2017", "Happiness Score_2018",
                   "Happiness Score_2019", "Happiness Score_2020", "Happiness Score_2021", "Happiness Score_2022"]

happinessscore_cleaned = happiness_score[columns_to_keep]

#rounding the score. 

happiness_round = happinessscore_cleaned.round(1)
happiness_mean = happinessscore_cleaned.round(1)

# Load the world shapefile
#We will use this later
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

#calculating the mean, to see what is the top 10 happiest countries

columns_mean = ["Happiness Score_2015", "Happiness Score_2016", "Happiness Score_2017", "Happiness Score_2018",
                   "Happiness Score_2019", "Happiness Score_2020", "Happiness Score_2021", "Happiness Score_2022"]

happiness_mean["Mean"] = happiness_round[columns_mean].mean(axis=1)

#Now with the mean, we can see which country has overall the highest happiness score. 
#We will create a top 10 happiest, and a top 10 saddest countries. 
#First, we will round the mean with 1 decimal. This will overall give a better look when we want to vizualize. 

happiness_mean = happiness_mean.round(1)
Happy_country = happiness_mean[["Country", "Mean"]]
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

#Lets create a world map. first we will call the data. 
# Load data
data = {
    "Country": [
        "Denmark", "Finland", "Switzerland", "Iceland", "Norway", "Netherlands", "Sweden", "Canada", "New Zealand",
        "Australia", "Israel", "Austria", "Costa Rica", "Mexico", "United States", "Brazil", "Ireland", "Belgium",
        "United Arab Emirates", "United Kingdom", "Singapore", "Panama", "Germany", "Chile", "France",
        "Argentina", "Uruguay", "Colombia", "Thailand", "Saudi Arabia", "Spain", "Malta", "El Salvador", "Uzbekistan",
        "Slovakia", "Japan", "South Korea", "Ecuador", "Bahrain", "Italy", "Bolivia", "Moldova", "Paraguay", "Kazakhstan",
        "Slovenia", "Lithuania", "Nicaragua", "Poland", "Kosovo", "Malaysia", "Jamaica", "Mauritius", "Estonia",
        "Latvia", "Philippines", "Romania", "Croatia", "Serbia", "Portugal", "Hungary", "Honduras", "Algeria", "Kyrgyzstan",
        "Montenegro", "Bosnia and Herzegovina", "Dominican Republic", "Greece", "Venezuela", "Indonesia", "Vietnam", "Mongolia",
        "Turkey", "Pakistan", "China", "Tajikistan", "Morocco", "Nigeria", "Nepal", "Jordan", "Albania", "Lebanon",
        "South Africa", "Cameroon", "Bulgaria", "Bangladesh", "Iran", "Iraq", "Ghana", "Armenia", "Tunisia", "Senegal",
        "Gabon", "Ivory Coast", "Ukraine", "Kenya", "Georgia", "Ethiopia", "Myanmar", "Sri Lanka", "Mali", "Cambodia",
        "Zambia", "Sierra Leone", "Egypt", "Guinea", "Burkina Faso", "Benin", "Uganda", "India", "Malawi", "Togo",
        "Zimbabwe", "Tanzania", "Afghanistan"
    ],
    "Mean": [
        7.6, 7.6, 7.5, 7.5, 7.5, 7.4, 7.4, 7.3, 7.3, 7.3, 7.2, 7.2, 7.1, 6.6, 7.0, 6.5, 7.0, 6.9, 6.7, 7.0, 5.3,
        6.5, 6.4, 7.0, 6.5, 6.6, 6.3, 6.4, 6.2, 6.2, 6.4, 6.4, 6.6, 6.2, 6.1, 6.2, 6.2, 5.8, 5.8, 5.7, 6.0, 6.1,
        6.1, 6.1, 6.1, 6.0, 5.9, 5.9, 5.8, 5.8, 5.8, 5.8, 5.8, 5.7, 5.6, 5.6, 5.6, 5.6, 5.5, 5.5, 5.4, 5.4, 5.4,
        5.4, 5.4, 5.4, 5.3, 5.3, 5.3, 5.3, 5.2, 5.2, 5.2, 5.2, 5.1, 5.0, 5.0, 4.9, 4.9, 4.8, 4.8, 4.8, 4.8, 4.7,
        4.7, 4.7, 4.7, 4.7, 4.6, 4.6, 4.6, 4.6, 4.5, 4.5, 4.5, 4.4, 4.4, 4.4, 4.4, 4.4, 4.3, 4.3, 4.3, 4.3, 4.3,
        4.3, 4.3, 4.2, 4.1, 3.8, 3.8, 3.7, 3.5, 3.1]}

# Create DataFrame
happy_country = pd.DataFrame(data)

# Merge with world DataFrame
world = world.merge(happy_country, how="left", left_on="name", right_on="Country")

# Plot
fig = px.choropleth(
    world,
    geojson=world.geometry,
    locations=world.index,
    title="Mean Score Happiness | Source:(Gcmadhan, 2021) ",
    color="Mean",
    hover_name="name",
    projection="natural earth",
    color_continuous_scale=px.colors.sequential.Viridis,
)

fig.update_geos(showcountries=True, countrycolor="black")

st.plotly_chart(fig)


pyo.plot(fig, filename='happiness_map.html', auto_open=False)

#Lets create a top 10

top_10_biggest = happiness_mean.nlargest(10, "Mean")
top_10_smallest = happiness_mean.nsmallest(10, "Mean")

# Print the top 10 rows
print(top_10_biggest)
print(top_10_smallest)

#Now lets convert the two dataframes together. 

top_10 = pd.concat([top_10_smallest, top_10_biggest])

#Streamlit layout

st.title("Can money buy happiness?")
st.text("There are alot of studies that have found a relationship between money")
st.text("and a good economy with happiness.According to this data, the countries")
st.text("with the hightest happiness score are in fact devolped countries.")
st.text("so,the data backes this up. ")

st.title("Easterlin Paradox")
st.text("The Easterlin Paradox is a theory where you look for a connection between happiness")
st.text ("and economis. The finding is formulated by professor Richard Easterlin. He was the")
st.text ("first economic to study happiness data.The Easterlin Paradox proves that ")
st.text("appiness varies directly with income, but over time happiness does not increase")
st.text("when income increases to a certain level.(Easterlni, R. 1974)")

st.write("--------")
image_path = r"C:\Users\Wendy\OneDrive\Afbeeldingen\2.jpg"
st.image(image_path, use_column_width=True)
st.write("--------")

st.title("People always get jealous")
st.text("The paradox states that if a person gets a higher income, and the people")
st.text("around them have the same raise, the person's happiness will most")
st.text("likely not increase. Over time, the paradox has been updated and the")
st.text("latest version of 2022 states that: There is still a lot if critcs on ")
st.text("the Paradox. They point at different studies, based on a short time period.")
st.text("In these short time periods, its been proven that people with.") 
st.text("more money are happier.But the Paradox focuses on the long term.")
st.text("(Easterlin & O’Connor, 2022)")
st.write("--------")
image_path = r"C:\Users\Wendy\OneDrive\Afbeeldingen\1.jpg"
st.image(image_path, use_column_width=True)
st.write("--------")
        
#_________________________________________________________________
st.title("Top ten countries: happiness score:")
st.text("In the previous map we had a quick overview, in the graph below you will")
st.text("see which countries have the highest score and which country has the lowest score.")
st.text("The yellow bar has the highest score, and the purple bar shows the lowest.")
st.markdown("<b> Source:</b>(Gcmadhan, 2021)", unsafe_allow_html=True)

#_________________________________________________________________
#Graph. In this section we will create a bar chart. We will use the mean of the happiness score. 
#WE use the mean, because the numbers through out the years don't difference much.

top_10.set_index("Country", inplace=True)

# Define a Streamlit slider to select the number of top countries to display

# Plotting the bar chart
plt.figure(figsize=(16, 8))
plt.bar(top_10.index, top_10["Mean"], color="Blue")

# Get the index of the country with the highest mean happiness score
idx_max = top_10["Mean"].idxmax()

# Get the index of the country with the lowest mean happiness score
idx_min = top_10["Mean"].idxmin()

# Setting color for the bar corresponding to the highest mean happiness score to red
plt.bar(idx_max, top_10.loc[idx_max, "Mean"], color="Red")

# Setting color for the bar corresponding to the lowest mean happiness score to blue
plt.bar(idx_min, top_10.loc[idx_min, "Mean"], color="Red")

# Adding labels and titles
plt.title("Mean Happiness Score of Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Mean Happiness Score")

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()

#moving the plot to Streamlit
# Get the index of the country with the highest mean happiness score
idx_max = top_10["Mean"].idxmax()

# Get the index of the country with the lowest mean happiness score
idx_min = top_10["Mean"].idxmin()

# Define a Streamlit slider to select the number of top countries to display
num_countries = st.slider('Select number of top countries to display:', min_value=5, max_value=10, value=20)

# Plotting the bar chart
plt.figure(figsize=(16, 8))
plt.bar(top_10.index[:num_countries], top_10["Mean"][:num_countries], color="Blue")

# Setting color for the bar corresponding to the highest mean happiness score to red
plt.bar(idx_max, top_10.loc[idx_max, "Mean"], color="gold")

# Setting color for the bar corresponding to the lowest mean happiness score to blue
plt.bar(idx_min, top_10.loc[idx_min, "Mean"], color="indigo")

# Adding labels and titles
plt.title("Mean Happiness Score of Top {} Countries".format(num_countries))
plt.xlabel("Country")
plt.ylabel("Mean Happiness Score")

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()

# Displaying the plot
plt.show()

# Moving the plot to Streamlit
st.pyplot(plt.gcf())

st.title("")
#_______________________________________________________________________________________________________________
#The bar chart is now working in streamlit. Let's build more structure and move on to the next topic.
#structure streamlit

#Income levels!

st.write("---")
st.title("Income and GDP")
#structure 

#Importing wrangled csv's from pythonfile: unemployed.

Income_data = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\Income.csv")
Unemployment = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\unemployment.csv")
Info_data = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\Backgroundinfo.csv")

#dropping na's

Income_data.dropna(inplace=True)

#counting and grouping the values in income level
income_level = Income_data['income level'].value_counts()

grouped_income = Income_data.groupby('income level')['country'].apply(list)

# Create pie chart data. We want to make it interactive, so that you can see each income value of each country
labels = [f"<b>{level}</b>" for level in grouped_income.index] 
values = [len(country_list) for country_list in grouped_income.values]
colors = {'High income': 'red', 'Lower middle income': 'blue', 'Low income': 'green', 'Upper middle income': 'gold'}

# Create hover text
hover_text = ['<br>'.join(country_list) for country_list in grouped_income.values]

# Plot the pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hovertext=hover_text)])

# Assign colors to each income level
fig.update_traces(marker=dict(colors=[colors[level] for level in grouped_income.index]))

# Display the Streamlit app
st.write("Hover over each income level to see the list of grouped countries.")
st.plotly_chart(fig, use_container_width=True)

#__________________________________________________________________________________________

GDP = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\GDP.vlean.csv")

# Creating DataFrame with provided GDP values
gdp_values = [
    14266499429.8746, 1692956646855.7, 2161483369422.01, 818426550206.45,
    400167196948.707, 424671765455.704, 282649838009.729, 3416645826052.87,
    28064529851.3098, 13164667626.9363, 1009398719033.08, 593348981537.661,
    248101705541.399, 4094563859.43556, 591718144602.141, 8341225241.45693,
    75732311666.039, 45567304608.4764, 29163782138.3415, 27366627153.0852]

Income_data = Income_data.rename(columns={'country': 'Country Name'})
GDP = GDP.rename(columns={'2022': 'GDP in US $ (2022)'})
GDP = GDP.rename(columns={'Mean': 'Happiness Score'})


# Merge the two DataFrames based on 'Country Name'
merged_df = pd.merge(GDP, Income_data, on='Country Name', how='inner')

# Create a scatter plot using Altair
scatter_plot = alt.Chart(merged_df).mark_circle(size=60).encode(
    x=alt.X('GDP in US $ (2022)', scale=alt.Scale(type='log')),
    y=alt.Y('Happiness Score', scale=alt.Scale(type='log')),
    color=alt.Color('income level', scale=alt.Scale(domain=['High income', 'Lower middle income', 'Low income'],
                                                    range=['red', 'blue', 'green']),
                   legend=alt.Legend(title='Income Level')),
    tooltip=['Country Name', 'GDP in US $ (2022)', 'Happiness Score']
).interactive()

# Streamlit UI
st.title('Scatter Plot of GDP vs Happiness')
st.write("Hover over the points to see country name, GDP, and happiness score.(World Bank Open Data, n.d.)")
st.write("Only the countries of the top 20 happiness score are portrayed. Egypt is not in")
st.write("the scatter, since it wasn't in many income group.No country in the top 20 were labeled as upper middle.")
st.altair_chart(scatter_plot, use_container_width=True)
#_______________________________________________________________________________________________________________
#Gross domestic product (GDP) is the monetary value of all finished goods 
#and services made within a country during a specific period.

st.text("Gross domestic product (GDP) is the monetary value of all finished goods,")
st.text("and services made within a country during a specific period.")
st.text("A high GDP will represents a good economy.(Fernando, J. 2024).")
st.write("--------")
st.text("In the previous graph we have discovered that Afghanitstan had the") 
st.text("lowest happiness score, and Denkmark has the highest. When we look")
st.text("at the scatter, it showes that Denmark has high income and a good gdp, although")
st.text("It doens't has the best gdp. This will also be more clear when we look at the ")
st.text("inflation of these countries. Afhanistan has a low happiness score, ")
st.text("but not the lowest GDP. This is because the happiness score ")
st.text("isn't measured on only the economy espects." )
#Graphs Glocal infation. Now we want to work eith different data: inflation. We will create a linegraph.
#_________________________________________________________________________________________________________________
st.title("Difference Between Developed Countries and Developing Countries")

image_path = r"C:\Users\Wendy\Downloads\Developed-Vs-Developing-Countries.jpg"
st.image(image_path, use_column_width=True)

st.text("Countries get divided in two categories. Wich are either devolped or devolping.")
st.text("This is mainly based on the economic status such as GDP, GNP, per capita income, ")
st.text("About industrialization, the standard of living. Developed countries have a better") 
st.text("economy and better technological aspects (S, 2020).")
st.text("There is a big difference between Developed Countries and develping countries.")
st.text("The develpoed countries are self-contained while devolping countries are not.")
st.markdown("----------")
st.text("Can poor countries even be happy? According to the Happiness index, poor countries")
st.text("have the lowest happiness score.Some studies suggestthat people in poorer countries")
st.text("were happier. But when we look deeper,some studies prove otherwise. For example,")
st.text("in Sub-Saharan Africa, where many countries are poor, people aren't as happy compared,")
st.text("to places like South America or Europe. Even though Africa has more poverty,")
st.text(" doesn't mean people there aren't happier or just as happy.")
st.text("This tells us that happiness isn't just about having money.")
st.text("Other things, like community support and quality of life,")
st.text("also play a big role in how happy people are.(Bundervoet, 2023)")


#________________________________________________________________________________________________________________________
st.write("---")
st.title("Global Inflation")
st.text("Here you can see the inflation growhth between the years 2015 and 2023.")
st.text("Pick three or more countries to your liking. Keep in mind that some countries")
st.text("have a too big inflation to be compared with a 'normaler rate'. ")
st.write("---")
st.text("Inflation levels of 1% to 2% per year are generally considered acceptable,")
st.text("while inflation rates greater than 3% to 4% can represent an overheating economy.")
st.write("---")
st.markdown("<b> The <span style='color:red;'>Red</span> line represents the normal inflation rate: 2% </b>", unsafe_allow_html=True)
st.markdown("<b> Source: (Global Inflation Dataset, 2024) </b>", unsafe_allow_html=True)

#note that we didn't give the dataframe a new name, since we will not use 2024 in any way. As you can see the year '2024'is now removed.
#now the dataframe is still a bit hard to read. 
#Now lets clean the data up again and removes all empty answers. 
#we do this by dropping the missing values
#We will do this so that the mean has the many amount of values per country. 

global_inflation = pd.read_csv(r"C:\Users\Wendy\OneDrive\Bureaublad\Python coding\Data viz\global_inflation_data.csv")

# List of countries
countries = ["Denmark", "Finland", "Switzerland", "Iceland", "Norway", "Netherlands", "Sweden", "Canada", "New Zealand",
             "Australia", "Israel", "Austria", "Costa Rica", "Mexico", "United States", "Brazil", "Ireland", "Belgium",
             "United Arab Emirates", "United Kingdom", "Singapore", "Panama", "Germany", "Chile", "France",
             "Argentina", "Uruguay", "Colombia", "Thailand", "Saudi Arabia", "Spain", "Malta", "El Salvador", "Uzbekistan",
             "Slovakia", "Japan", "South Korea", "Ecuador", "Bahrain", "Italy", "Bolivia", "Moldova", "Paraguay", "Kazakhstan",
             "Slovenia", "Lithuania", "Nicaragua", "Poland", "Kosovo", "Malaysia", "Jamaica", "Mauritius", "Estonia",
             "Latvia", "Philippines", "Romania", "Croatia", "Serbia", "Portugal", "Hungary", "Honduras", "Algeria", "Kyrgyzstan",
             "Montenegro", "Bosnia and Herzegovina", "Dominican Republic", "Greece", "Venezuela", "Indonesia", "Vietnam", "Mongolia",
             "Turkey", "Pakistan", "China", "Tajikistan", "Morocco", "Nigeria", "Nepal", "Jordan", "Albania", "Lebanon",
             "South Africa", "Cameroon", "Bulgaria", "Bangladesh", "Iran", "Iraq", "Ghana", "Armenia", "Tunisia", "Senegal",
             "Gabon", "Ivory Coast", "Ukraine", "Kenya", "Georgia", "Ethiopia", "Myanmar", "Sri Lanka", "Mali", "Cambodia",
             "Zambia", "Sierra Leone", "Egypt", "Guinea", "Burkina Faso", "Benin", "Uganda", "India", "Malawi", "Togo",
             "Zimbabwe", "Tanzania", "Afghanistan"]

# Filtering the DataFrame
filtered_GF = global_inflation[global_inflation['country_name'].isin(countries)]
# Selecting columns from 2015 to 2023
columns_to_select = [str(year) for year in range(2015, 2024)]

# Selecting the filtered DataFrame with only the desired columns
filtered_inflation = filtered_GF[["country_name"] + columns_to_select]
#Drop nans
filtered_inflation.dropna(inplace=True)

# Multiselect widget to select countries
selected_countries = st.multiselect('Select Countries', filtered_inflation['country_name'])

# Filter data for selected countries
filtered_inflation = filtered_inflation[filtered_inflation['country_name'].isin(selected_countries)]

if not filtered_inflation.empty:
    # Melt the DataFrame to long format
    filtered_inflation_melted = filtered_inflation.melt(id_vars='country_name', var_name='Year', value_name='Inflation')

    # Convert Year column to datetime type
    filtered_inflation_melted['Year'] = pd.to_datetime(filtered_inflation_melted['Year'])

    # Create an Altair chart
    chart = alt.Chart(filtered_inflation_melted).mark_line().encode(
        x='Year:T',
        y='Inflation:Q',
        color='country_name:N',
        tooltip=['country_name', 'Year', 'Inflation'])

    # Add a horizontal line at y=2
    horizontal_line = alt.Chart(pd.DataFrame({'y': [2]})).mark_rule(color='red', strokeDash=[5,5]).encode(
        y='y:Q')

    # Combine the chart and horizontal line
    st.altair_chart(chart + horizontal_line, use_container_width=True)
    
else:
    st.write('Please select at least one country to plot.')
    
st.write("--------")
st.text("We can see the groth of the inflation of each indivual country and compare them with")
st.text("three others,but lets place the top 20 (saddest/happiest) in a scattor plot,")
st.text("so we can quickly see how the countries are distanced from the annual inflation ")
st.text("rate of 2 procent.We will use the data from 2022.")
st.text("The closer they are to the red line,the better.")
global_inflation = global_inflation.rename(columns={'country_name' : 'Country'})

# Countries list
countries_to_keep = ['Afghanistan', 'Australia', 'Canada', 'Denmark', 'Finland', 'India', 'Iceland', 'Malawi', 'Netherlands', 'New Zealand',
                     'Norway', 'Sierra Leone', 'Sweden', 'Switzerland', 'Tanzania', 'Togo', 'Uganda', 'Zambia', 'Zimbabwe']

# Filtering DataFrame for selected countries
filtered_global_inflation = global_inflation[global_inflation['Country'].isin(countries_to_keep)]

# Calculate the difference from the average (2)
filtered_global_inflation['Difference'] = abs(filtered_global_inflation['2022'] - 2)

# Plotly scatter plot with hover functionality
fig = px.scatter(filtered_global_inflation, x='Country', y='Difference',
                 hover_name='Country',
                 labels={'Country': 'Country', 'Difference': 'Difference from Average (2)', '2022': 'Inflation (2022)'},
                 title='Inflation Score Deviation from Average (2022)')

# Add a line for the main inflation
fig.add_hline(y=2, line_dash="dash", line_color="red", annotation_text="Tageted inflation rate (2%) (Consumer Price Index)", annotation_position="top right")

# Customize the y-axis range
fig.update_yaxes(type="log")

fig.update_layout(xaxis_tickangle=-90)

# Display the plot using Streamlit
st.plotly_chart(fig)

#Below is just text in streamlit.
#More strucute  
st.write("---")
st.title("How is it all connected?")
st.text("When we look through the economic lense, we can see that the countries ")
st.text("with the highest happiness scores are in the high income group, ")
st.text("and have a reletive high GDP.")
st.text("However, in 2022 Tanzania had the lowest (and best) inflation rate, but had a low") 
st.text("happpiness score and.a lower income than happier countires.")
st.markdown("---------")
st.text( "When we dive deeper in the inflation rates, 1% - 2% is considered good,")
st.text("while things get overheatedat 3% or more. Things will get more expsenive ")
st.text("and money will be less worth. So with this datastory about the controversy whether") 
st.text("money equals happiness, my answer, based on data and studies, is that it can buy")
st.text("happiness and makes lifes easier,but it doesn't give a complete answer.")

#Structure and Reflection. (There are no more tech codes, just the reflection for design.)
st.write("---")
st.title("My Perspective")
st.markdown("<b> We will use the Data Perspective Model </b>", unsafe_allow_html=True)
st.write("-------")
st.markdown("<b> Econmic angle </b>", unsafe_allow_html=True)
st.text("Devolped countries have overall a higher gdp, better happiness score and higher")
st.text("income. Tenzenia, Switerland and Norway overall have the best inflation,")
st.text("While Denmark has the best happiness score, even though there is hyperinflation.")
st.text("Note that India has the best gdp, but is in de top 10 of lowest happiness score.")
st.text("When we look through the economic lens, there are defenitly some connections with")
st.text("economic and happiness but just saying money can buy happiness ")
st.text("is not giving the whole picture.Devolping countries can in fact be happy,")
st.text("but their happiness is not deplied in the same categories")
#Imagine to and the topic
image_path = r"C:\Users\Wendy\Downloads\shutterstock_2154195865-1.png"
st.image(image_path, use_column_width=True)
#Starting a new topic
st.write("-------")
st.markdown("<b> Ethical and Philosophial angle </b>", unsafe_allow_html=True)
st.text("It's not etical to only look at economic and financial aspects,")
st.text("since the happiness score is not only based on that, ")
st.text("It has more aspects, such as goverment, work balance, safety in a country,")
st.text("culture, satifaction in live, ect. ")
st.text("many of these values differ in devolped and devolping countries.")
st.text("The words have different meanings for each country.")
st.text("For example to happiness scores are based on social support, healthy life expectancy,")
st.text("freedom, generosity, and corruption.")
st.write("-------")
st.text("Many of these factors are completly different for devolped and devolping countries") 
st.text("Yet, they use the same score ranking,")
st.text("The ethics of ranking developing and developed countries using the same measurements")
st.text("can be a complex issue.The Happiness Report Score (going from 1 to 10) measures")
st.text("how happy countries are in factors like social support, healthy life expectancy,")
st.text("freedom, generosity, and corruption. But these things mean different things")
st.text("for devdloping and developed countries Both have different socio-economic factors,")
st.text("so the score will automaticaly be different.")
st.text("The problem with the World Happiness Report is that they both use the same values")
st.text("for both level of countries.")
#Imagine to and the topic
image_path = r"C:\Users\Wendy\Downloads\shutterstock-2072700533-1-1657500298.jpg"
st.image(image_path, use_column_width=True)
#Starting a new topic
st.write("-------")
st.markdown("<b> Temporality angle </b>", unsafe_allow_html=True)
st.text("As the data proves, the devolping countries has the lowest happiness score.")
st.text("It's not ethical to compare a devolped and devolping country on the same scale.")
st.text("The nations gave numbers from 1 to 10 based on these categories,")
st.text("but comparing them can be considered unethical, since it can be interpreted")
st.text("in a different way, or nations have different valuwes to each category.")
st.write("-------")
st.text("Economics are shifting the whole time. GDP and inflation can chance over time.")
st.text("This has impact on the Happiness Score.And if over time, devolping countries are")
st.text("more devolped, it can also have impact.")
st.text("It's important to note that the studies and dataframes that are used")
st.text("are reflecting on a certain time period and may not be applied on daily bases")
st.text("For example, the study of the Easterlin Paradox has first taken place in 1974.") 
st.text("Overtime people have critized the study, since it didn't apply to the whole global.")
#Imagine to and the topic
image_path = r"C:\Users\Wendy\Downloads\future-of-on-demand.jpg"
st.image(image_path, use_column_width=True)
#Starting a new topic
st.write("-------")
st.markdown("<b> Technical angle </b>", unsafe_allow_html=True)
st.text("There are multiple studies about economy, happiness and a possbible")
st.text("relation between them.To vizualize and clean raw data, its important to")
st.text("be aware what story you want to tell, if you leave a certain value out,")
st.text("than the story will be changed.There for, I am aware that i am only showing")
st.text("one part of the story, but it doesn't tell the whole picture.")
#Imagine to and the topic
image_path = r"C:\Users\Wendy\Downloads\image.jpg"
st.image(image_path, use_column_width=True)
#Starting a new topic
st.write("-------")
#Structure
st.title("Resources")
st.text("Easterlin, R. A., & O’Connor, K. J. (2022). The Easterlin Paradox. In Springer eBooks (pp. 1–25). https://doi.org/10.1007/978-3-319-57365-6_184-2")
st.text("Fernando, J. (2024, February 29). Gross domestic product (GDP) formula and how to use it. Investopedia. https://www.investopedia.com/terms/g/gdp.asp#:~:text=Gross%20domestic%20product%20is%20the,country%20during%20a%20specific%20period.")
st.text("Models of development - Differences in levels of development between developing countries - Higher Geography Revision - BBC Bitesize. (n.d.). BBC Bitesize. https://www.bbc.co.uk/bitesize/guides/zt666sg/revision/1")
st.text("World Bank Open Data. (n.d.). World Bank Open Data. https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=XM")
st.text("Gcmadhan. (2021, June 28). World Happiness Index Report. Kaggle. https://www.kaggle.com/code/gcmadhan/world-happiness-index-report")
st.text("Income and happiness correlation. (2020, September 22). Kaggle. https://www.kaggle.com/datasets/levyedgar44/income-and-happiness-correction")
st.text("Global Inflation Dataset. (2024, February 16). Kaggle. https://www.kaggle.com/datasets/sazidthe1/global-inflation-data")
st.text("About | The World Happiness Report. (n.d.). https://worldhappiness.report/about/#:~:text=We%20use%20observed%20data%20on,freedom%2C%20generosity%2C%20and%20corruption.")
st.text("S, S. (2020, April 17). Difference Between Developed Countries and Developing Countries (with Comparison Chart) - Key Differences. Key Differences. https://keydifferences.com/difference-between-developed-countries-and-developing-countries.html#Conclusion")
st.text("Bundervoet, T. (2023, October 2). Poor but happy? World Bank Blogs. https://blogs.worldbank.org/africacan/poor-but-happy")