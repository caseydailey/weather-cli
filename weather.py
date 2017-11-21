import argparse
from src.api import get_weather
from src.views import weather_report



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find out if umbrella, jacket, or sunglasses are needed for a given zip code.')
    parser.add_argument('--zip', dest='zip_code')

    args = parser.parse_args()

    if args.zip_code:
        weather_dict = get_weather(args.zip_code)
        print(weather_report(weather_dict))
    else:
        parser.print_usage()
