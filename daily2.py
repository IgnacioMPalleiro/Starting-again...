weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}
print("What's te weather like today?" "1. Sunny \n 2. Rainy\n 3. Cloudy\n 4. Snowy")
weather = input("Choose 1, 2, 3, or 4: ")
if weather in weather_activities:
    print(weather_activities[weather])
