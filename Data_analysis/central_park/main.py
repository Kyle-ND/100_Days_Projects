import pandas

# read data from squirrel data
data = pandas.read_csv('./Data_analysis/central_park/squirrel_data.CSV')

# get number of black squirrels
black =  data[data["Primary Fur Color"] == "Black"]
number_black = len(black.index)

# get number of grey squirrels

Gray = data[data["Primary Fur Color"] == "Gray"]
number_grey = len(Gray.index)

# get number of cinnamon colored squirrels

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
number_cinnamon = len(cinnamon.index)

# create a new data frame
data_frame = {
    'Fur Color' : ["Black","Grey","Cinnamon"],
    'Count': [number_black,number_grey,number_cinnamon]
    }

d = pandas.DataFrame(data_frame)

# save data frame to a csv file 
d.to_csv('./Data_analysis/central_park/squirrel_count.csv')