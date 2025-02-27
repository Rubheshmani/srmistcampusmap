from flask import Flask, render_template
import folium
from folium.plugins import Draw

app = Flask(__name__)

@app.route('/')
def index():
    latitude = 12.8281
    longitude = 80.0359
    
    srmist_map = folium.Map(location=[latitude, longitude], zoom_start=17)
    folium.TileLayer('OpenStreetMap').add_to(srmist_map)

    folium.Marker(
        [latitude, longitude],
        popup=folium.Popup("<b>SRMIST Kattankulathur Campus</b><br>Welcome to SRMIST!", max_width=200),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(srmist_map)

    # Draw control options
    draw = Draw(
        export=True,
        draw_options={
            'polyline': True,
            'polygon': True,
            'circle': True,
            'rectangle': True,
            'marker': True,
            'circlemarker': True
        },
        edit_options={
            'edit': True  # Enable editing of drawn shapes
        }
    )
    draw.add_to(srmist_map)

    # Predefined shapes for demonstration (polygon, rectangle)
    folium.Polygon(
        locations=[[12.8285, 80.0359], [12.8285, 80.0365], [12.8280, 80.0365], [12.8280, 80.0359]],
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.3,
        popup=folium.Popup("This is a predefined polygon", max_width=200)
    ).add_to(srmist_map)

    folium.Rectangle(
        bounds=[[12.8275, 80.0355], [12.8280, 80.0360]],
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.3,
        popup=folium.Popup("This is a predefined rectangle", max_width=200)
    ).add_to(srmist_map)

    # Save the map as an HTML file in the static folder
    srmist_map.save('./static/srmist_map.html')

    # Render the template
    return render_template("index.html", map_html='srmist_map.html')

if __name__ == "__main__":
    app.run(debug=True)
