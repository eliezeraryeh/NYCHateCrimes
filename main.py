import folium
import pandas as pd


pct_geo = f"./Data/Police Precincts.geojson"
hate_crimes = pd.read_csv('./Data/precinct_totals.csv',
                          dtype={'precinct': str})


m = folium.Map(location=[40.7212404496413, -73.97914804524488], zoom_start=10,
               tiles='CartoDB positron')

folium.Choropleth(
    geo_data=pct_geo,
    name="choropleth",
    data=hate_crimes,
    columns=["precinct", "total"],
    key_on="feature.properties.precinct",
    line_color='black',
    line_weight=1,
    fill_color="YlGn",
    fill_opacity=0.7,
    smooth_factor=1,
    line_opacity=0.2,
    legend_name="NYC Hate Crime Arrests 2017- Q3 2022",
    control=False,
    ).add_to(m)

folium.LayerControl().add_to(m)

m.save("out.html")
