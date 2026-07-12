
majin_list = ["kid_buu", "majin_buu", "super_buu", "evil_buu", "majin_vegeta", "asaf dego"]

for majin in majin_list:
    if majin.find("_") != -1:
        print (majin + " " + majin[:majin.find("_")])
    
    else:
        print (majin + " " + majin[0:3])
