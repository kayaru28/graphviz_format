import numpy as np
import math
#https://www.benricho.org/chimei/latlng_data.html
class prefectures:
    data=np.array([['北海道',43.063968,141.347899]])
    data=np.append(data,[['青森県',40.824623,140.740593]], axis=0)
    data=np.append(data,[['岩手県',39.703531,141.152667]], axis=0)
    data=np.append(data,[['宮城県',38.268839,140.872103]], axis=0)
    data=np.append(data,[['秋田県',39.718600,140.102334]], axis=0)
    data=np.append(data,[['山形県',38.240437,140.363634]], axis=0)
    data=np.append(data,[['福島県',37.750299,140.467521]], axis=0)
    data=np.append(data,[['茨城県',36.341813,140.446793]], axis=0)
    data=np.append(data,[['栃木県',36.565725,139.883565]], axis=0)
    data=np.append(data,[['群馬県',36.391208,139.060156]], axis=0)
    data=np.append(data,[['埼玉県',35.857428,139.648933]], axis=0)
    data=np.append(data,[['千葉県',35.605058,140.123308]], axis=0)
    data=np.append(data,[['東京都',35.689521,139.691704]], axis=0)
    data=np.append(data,[['神奈川県',35.447753,139.642514]], axis=0)
    data=np.append(data,[['新潟県',37.902418,139.023221]], axis=0)
    data=np.append(data,[['富山県',36.695290,137.211338]], axis=0)
    data=np.append(data,[['石川県',36.594682,136.625573]], axis=0)
    data=np.append(data,[['福井県',36.065219,136.221642]], axis=0)
    data=np.append(data,[['山梨県',35.664158,138.568449]], axis=0)
    data=np.append(data,[['長野県',36.651289,138.181224]], axis=0)
    data=np.append(data,[['岐阜県',35.391227,136.722291]], axis=0)
    data=np.append(data,[['静岡県',34.976978,138.383054]], axis=0)
    data=np.append(data,[['愛知県',35.180188,136.906565]], axis=0)
    data=np.append(data,[['三重県',34.730283,136.508591]], axis=0)
    data=np.append(data,[['滋賀県',35.004531,135.86859]], axis=0)
    data=np.append(data,[['京都府',35.021004,135.755608]], axis=0)
    data=np.append(data,[['大阪府',34.686316,135.519711]], axis=0)
    data=np.append(data,[['兵庫県',34.691279,135.183025]], axis=0)
    data=np.append(data,[['奈良県',34.685333,135.832744]], axis=0)
    data=np.append(data,[['和歌山県',34.226034,135.167506]], axis=0)
    data=np.append(data,[['鳥取県',35.503869,134.237672]], axis=0)
    data=np.append(data,[['島根県',35.472297,133.050499]], axis=0)
    data=np.append(data,[['岡山県',34.661772,133.934675]], axis=0)
    data=np.append(data,[['広島県',34.396560,132.459622]], axis=0)
    data=np.append(data,[['山口県',34.186121,131.470500]], axis=0)
    data=np.append(data,[['徳島県',34.065770,134.559303]], axis=0)
    data=np.append(data,[['香川県',34.340149,134.043444]], axis=0)
    data=np.append(data,[['愛媛県',33.84166,132.765362]], axis=0)
    data=np.append(data,[['高知県',33.559705,133.53108]], axis=0)
    data=np.append(data,[['福岡県',33.606785,130.418314]], axis=0)
    data=np.append(data,[['佐賀県',33.249367,130.298822]], axis=0)
    data=np.append(data,[['長崎県',32.744839,129.873756]], axis=0)
    data=np.append(data,[['熊本県',32.789828,130.741667]], axis=0)
    data=np.append(data,[['大分県',33.238194,131.612591]], axis=0)
    data=np.append(data,[['宮崎県',31.911090,131.423855]], axis=0)
    data=np.append(data,[['鹿児島県',31.560148,130.557981]], axis=0)
    data=np.append(data,[['沖縄県',26.212401,127.680932]], axis=0)

    ERROR_CODE      = -100
    DATA_COL_NAME   =  0
    DATA_COL_LAT    =  1
    DATA_COL_LON    =  2
    STANDERDIZE     =  10

    def print_data(self):
        print(self.data)

    def get_code(self,name):
        num = 0
        for prefecture in self.data:
            if prefecture[self.DATA_COL_NAME]==name:
                return num
            num = num + 1
        return self.ERROR_CODE

    def get_name(self,code):
        return self.data[code][self.DATA_COL_NAME]

    # Oval shape not considered
    def get_distance(self,code_1,code_2):
        longitude_1 = float(self.data[code_1][self.DATA_COL_LON])
        latitude_1  = float(self.data[code_1][self.DATA_COL_LAT])
        longitude_2 = float(self.data[code_2][self.DATA_COL_LON])
        latitude_2  = float(self.data[code_2][self.DATA_COL_LAT])
        distance    = (longitude_1 - longitude_2)**2 + (latitude_1 - latitude_2)**2

        return distance

    def get_standerdized_distance(self,code_1,code_2):
        return (math.log10(self.get_distance(code_1,code_2))/10+2.5)  # / self.STANDERDIZE )

