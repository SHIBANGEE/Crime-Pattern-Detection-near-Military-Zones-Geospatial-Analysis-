import pandas as pd
import folium
from sklearn.cluster import KMeans

# Step 1: Load data
df = pd.read_csv("crime_data_near_base.csv")
print("Data Loaded:\n", df.head())

# Step 2: K-Means clustering based on coordinates
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df[['latitude', 'longitude']])

# Step 3: Create base map centered on the mean location
center_lat = df['latitude'].mean()
center_lon = df['longitude'].mean()
map = folium.Map(location=[center_lat, center_lon], zoom_start=11)

# Step 4: Add points to the map
colors = ['red', 'blue', 'green']
for i, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=6,
        color=colors[row['cluster']],
        fill=True,
        fill_opacity=0.7,
        popup=f"Incident: {row['incident_type']}"
    ).add_to(map)

# Step 5: Save the map
map.save("crime_clusters_map.html")
print("Map saved to crime_clusters_map.html. Open it in your browser.")
