import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")

        self.city_label = tk.Label(root, text="Enter city:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            self.weather_label.config(text="Please enter a city.")
            return

        api_key = "1edf289b7bc3b168e4d1518bf6ae852f" 
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  # Use metric units for Celsius
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = f"Weather in {data['city']['name']}"

            temperatures = [entry['main']['temp'] for entry in data['list']]
            times = [entry['dt_txt'] for entry in data['list']]

            self.plot_temperature(times, temperatures)

            self.weather_label.config(text=weather_info)
        else:
            self.weather_label.config(text="City not found or API error.")

    def plot_temperature(self, times, temperatures):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(times, temperatures, marker='o', linestyle='-', color='b')
        ax.set_xlabel('Time')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Temperature Forecast')
        ax.grid()
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
