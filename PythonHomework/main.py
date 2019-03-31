import requests
import json
from GUI import *
from classes import *



#Get the weather report of Hefei
r_day = requests.get('https://free-api.heweather.net/s6/weather/forecast?location=合肥&key=90a2d6b5f3864f9cb2b5d591201e867a')
r_life = requests.get('https://free-api.heweather.net/s6/weather/lifestyle?location=合肥&key=e8410d236ac043bbb9939bd536e2e646')
r_air = requests.get('https://free-api.heweather.net/s6/air/now?location=合肥&key=e8410d236ac043bbb9939bd536e2e646')
#Use json to parse
hjson_day = json.loads(r_day.text)
hjson_life = json.loads(r_life.text)
hjson_air = json.loads(r_air.text)
#print(hjson_air)

#用于气温分析的对象初始化
weather_analysis = WeatherAnalysis(hjson_day['HeWeather6'][0]['daily_forecast'][0],
                                   hjson_day['HeWeather6'][0]['daily_forecast'][1],
                                   hjson_day['HeWeather6'][0]['daily_forecast'][2])
analysis_text = "三天平均气温： "+str(weather_analysis.average_tmp())+"\n"
analysis_text = analysis_text+"三天温差: "+str(weather_analysis.tmp_difference())+"\n"
#print(weather_analysis.realtime)
#print(hjson_life)
#截取response中的文本，将文本调整好格式后提供给GUI画布
day0 = hjson_day['HeWeather6'][0]['daily_forecast'][0]
life = hjson_life['HeWeather6'][0]['lifestyle']
day1 = hjson_day['HeWeather6'][0]['daily_forecast'][1]

day0_text = "气温： "+day0['tmp_max']+" -- "+day0['tmp_min']+"\n"
day0_text = day0_text+"日间天气： "+day0['cond_txt_d']+"\n"
day0_text = day0_text+"夜间天气： "+day0['cond_txt_n']+"\n"
day0_text = day0_text+"湿度： "+day0['hum']+"％\n"
day0_text = day0_text+"风向： "+day0['wind_dir']+"\n"
day0_text = day0_text+"风力： "+day0['wind_sc']+"\n"
day0_text = day0_text+"UV指数： "+day0['uv_index']+"\n"

life_text = "舒适指数： "+life[0]['brf']+"\n"+"     "+life[0]['txt']+"\n"
life_text = life_text+"穿衣指数： "+life[1]['brf']+"\n"+"     "+life[1]['txt']+"\n"
life_text = life_text+"流感指数： "+life[2]['brf']+"\n"+"     "+life[2]['txt']+"\n"
life_text = life_text+"运动指数： "+life[3]['brf']+"\n"+"     "+life[3]['txt']+"\n"
life_text = life_text+"旅行指数： "+life[4]['brf']+"\n"+"      "+life[4]['txt']+"\n"
life_text = life_text+"紫外线指数： "+life[5]['brf']+"\n"+"     "+life[5]['txt']+"\n"
life_text = life_text+"洗车指数： "+life[6]['brf']+"\n"+"     "+life[6]['txt']+"\n"
life_text = life_text+"空气质量： "+life[7]['brf']+"\n"+"     "+life[7]['txt']+"\n"

day1_text = "气温： "+day1['tmp_max']+" -- "+day1['tmp_min']+"\n"
day1_text = day1_text+"日间天气： "+day1['cond_txt_d']+"\n"
day1_text = day1_text+"夜间天气： "+day1['cond_txt_n']+"\n"
day1_text = day1_text+"湿度： "+day1['hum']+"％\n"
day1_text = day1_text+"风向： "+day1['wind_dir']+"\n"
day1_text = day1_text+"风力： "+day1['wind_sc']+"\n"
day1_text = day1_text+"UV指数： "+day1['uv_index']+"\n"

#启动GUI
weather_app = WeatherApp()
for_activity = {'tmp_max':float(day0['tmp_max']),
                'tmp_min':float(day0['tmp_min']),
                'hum':float(day0['hum']),
                'wind_spd':day0['wind_spd'],
                'aqi':float(hjson_air['HeWeather6'][0]['air_now_city']['aqi'])}

weather_app.input(day0_text,day1_text,life_text,analysis_text,for_activity)
weather_app.gui_arrange()
weather_app.box_init()
weather_app.button()

tkinter.mainloop()
