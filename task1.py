
majin_list = ["kid_buu", "majin_buu", "super_buu", "evil_buu", "majin_vegeta"]

for majin in majin_list:
    if majin.find("_"):
        print (majin + " " + majin[:majin.find("_")])
    
    else:
        print (majin[:3])
