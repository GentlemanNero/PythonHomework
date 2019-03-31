import tkinter
import tkinter.messagebox
class WeatherApp(object):
    def __init__(self):
        #创建主窗口
        self.root = tkinter.Tk()
        #给主窗口设置标题
        self.root.title("合肥小天气")
        #主窗口尺寸
        self.root.geometry("800x800+300+0")
    def box_init(self):
        #活动分析 文本框初始化
        self.box = tkinter.Entry(self.root, show=None)
        self.box.place(x=500, y=450)
    def input(self,day0,day1,life,analysis,for_activity):
        #输入：今日天气，明日，今日生活指数，用于活动分析的今日天气
        self.day0 = day0
        self.day1 = day1
        self.life = life
        self.analysis = analysis
        self.for_activity = for_activity
    #布局
    def activity_analysis(self):
        #活动分析 输入文本分析
        #result_text:用于显示结果 初始化为空
        result_text = ""

        activity = self.box.get()
        if(activity=="跑步"):
            if(self.for_activity['tmp_min']) > 25:
                result_text = result_text+"今日气温过高，跑步时注意防暑，尽量选择在清晨或夜间进行\n"
            elif( self.for_activity['tmp_max']<0 ):
                result_text = result_text+"今日气温过低，注意保暖\n"
            else:
                result_text = result_text+"今日天气适宜跑步\n"
            if(self.for_activity['aqi']>100):
                result_text = result_text+"今日空气质量较差，不适宜跑步\n"
        if (activity == "骑车"):
            if ( float(self.for_activity['wind_spd'])>11):
                result_text = result_text+"今日风力较强，骑车容易疲劳\n"
            if (self.for_activity['aqi'] > 100):
                result_text = result_text + "今日空气质量较差，不适宜骑车\n"
            if(result_text ==""):
                result_text = result_text + "今日天气适宜骑车\n"
        tkinter.messagebox.showinfo("活动分析",result_text)

    def gui_arrange(self):
        #当前天气标签及画布
        L_day0_weather_tag = tkinter.Label(self.root, text = "当前天气")
        L_day0_weather_tag.place(x=0,y=70)
        L_day0_weather = tkinter.Canvas(self.root,width = 200,height = 290,background = "white")
        L_day0_weather.create_text(60,75,text = self.day0)
        L_day0_weather.place(x=0,y=100)
        #生活指数 标签及画布设置
        L_life_tag = tkinter.Label(self.root, text="生活指数")
        L_life_tag.place(x=230,y=70)
        L_life = tkinter.Canvas(self.root, width=540, height=290, background="white")
        L_life.create_text(280, 150, text=self.life)
        L_life.place(x=230, y=100)
        #明日天气 标签
        L_day1_weather_tag = tkinter.Label(self.root, text = "明日天气")
        L_day1_weather_tag.place(x=0, y=420)
        #明日天气 画布
        L_day1 = tkinter.Canvas(self.root, width=200,height=200, background="white")
        L_day1.create_text(65, 75, text=self.day1)
        L_day1.place(x=0,y=450)
        #数字分析 标签及画布设置
        L_analysis_tag = tkinter.Label(self.root, text="数字分析")
        L_analysis_tag.place(x=230, y=420)
        L_analysis = tkinter.Canvas(self.root, width = 200,height =200, background="white")
        L_analysis.create_text(110,40,text = self.analysis)
        L_analysis.place(x=230,y=450)
        #活动分析 标签设置
        L_activity_analysis = tkinter.Label(self.root, text="活动分析")
        L_activity_analysis.place(x=500,y=420)


    def button(self):
        activity_button = tkinter.Button(self.root, text="确认", command=self.activity_analysis)
        activity_button.place(x=670,y=450)
