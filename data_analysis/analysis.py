import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place






players_data=pd.read_csv("csv_files/basketball_players.csv")
master = pd.read_csv("csv_files/basketball_master.csv")

#Mean and Median
min_points=players_data['points'].mean()
median_points=players_data['points'].median()

# print(f'Mean: {min_points}, Median: {median_points}')


#Highest number of scores
highest_score=players_data["points"].max()

#mergening player with master
player_master=pd.merge(players_data, master,left_on="playerID", right_on="bioID")

sortedPlayerMaster=player_master.sort_values(by="points",ascending=False).head(10)

#making a condition to select the highest player
condition1=sortedPlayerMaster['points']==highest_score

#applying the condition
player_with_highest_score=sortedPlayerMaster.where(condition1)

# print(player_with_highest_score[['firstName','lastName','year']])




#Producing a boxplot that shows the distribution of total points, total assists, and total rebounds
# sns.boxplot(data=player_master[['rebounds','points','assists']],palette=sns.color_palette("husl", 9),orient='h')
# plt.show()




#Median of points scored per year, over time

#first grouping the points per year and finding the median
group_by_year=player_master[['year','points']].groupby('year').median()
#resetting the index
# group_by_year=group_by_year.reset_index()
# sns.regplot(data=group_by_year,x='year',y='points').set_title('Median Points per Year')
# plt.show()




# PART II - COME UP WITH SUPPORTING EVIDENCE



#creating a new column ---pointsPerAttempt
#pointsPerAttempt= points/(field goal attempt + free throw attempts)
# player_master["pointsPerAttempt"]=player_master['points']/(player_master['fgAttempted']+player_master['ftAttempted'])
# sns.regplot(data=player_master[["points","pointsPerAttempt"]],x="points",y="pointsPerAttempt").set_title("Points vs Points per Attempt")
# plt.show()





#Performance in statistical categories

#grouping the players by playerID and finding the average of each statistical category
# groupedCategories=player_master[["playerID","points","blocks","rebounds","steals","assists"]].groupby("playerID").mean()
# sns.boxplot(data=groupedCategories)
# plt.show()



#Three Point Shot

#first group the data by "lgID" ---league
#then we find the mean of three point shots attempted per league
league_three_point=player_master[["lgID","threeAttempted"]].groupby("lgID").mean()

league_three_point=league_three_point.reset_index()
# sns.barplot(data=league_three_point,x='lgID',y='threeAttempted').set_title('Three-point shots across the leagues')
# plt.show()






# #three-point shots across NBA throughout the years
# #first select only NBA players
# nba=player_master[player_master["lgID"]=="NBA"]

# #finding the average of the three-point shots of NBA players throughout the years
# nba_three_shot=nba[["year","threeAttempted"]].groupby("year").mean()
# nba_three_shot=nba_three_shot[nba_three_shot["threeAttempted"]>0]
# nba_three_shot=nba_three_shot.reset_index()
# sns.regplot(data=nba_three_shot,x="year",y="threeAttempted").set_title("Average of NBA three-point scores per year, over time")
# plt.show()






#THE GOAT

#merging players withe awards
awards=pd.read_csv("csv_files/basketball_awards_players.csv")
#inner join
player_awards=pd.merge(player_master,awards,on="playerID")
#grouping the players by "playerID" and count them == the number of awards they have
grouped_player_awards=player_awards.groupby("playerID").size().reset_index(name="number_of_awards")
grouped_player_awards=grouped_player_awards.sort_values(by="number_of_awards",ascending=False).head(5)

# sns.barplot(data=grouped_player_awards,x="playerID",y="number_of_awards")
# plt.show()

#to get the full name of the greatest players
#we merge with the players data
greatest=pd.merge(grouped_player_awards, player_master,on="playerID")

# print(greatest[["playerID","fullGivenName","number_of_awards"]].head(50))



#Players who came from a similar location
#group by home city and home state 
grouped_by_place=player_master.groupby(["hsCity","hsState"]).size().reset_index(name="count")
grouped_by_place=grouped_by_place.sort_values('count',ascending=False)
#the location with the most number of players
most_players_home=grouped_by_place.head(1)

#most players are from Chicago, IL
#getting stats about those players
most_players_home=most_players_home.reset_index()
cityName=most_players_home["hsCity"][0]
stats_chicago=player_master[player_master["hsCity"]==cityName]

#stat1 --group by high school
high_stats=stats_chicago[["highSchool"]].groupby("highSchool").size().reset_index(name="player_count")
#top most attended schools
high_stats=high_stats.sort_values('player_count',ascending=False).head(3)
# sns.barplot(data=high_stats,x="highSchool",y="player_count").set_title(f"Top high schools for the city with most players - {cityName} ")
# plt.show()

#stat2 --group by college
college_stats=stats_chicago[["college"]].groupby("college").size().reset_index(name="player_count")
college_stats=college_stats.sort_values('player_count',ascending=False).head(3)
color_p=sns.color_palette("hls", 8)
# sns.barplot(data=college_stats,x="college",y="player_count",palette=color_p).set_title(f"Top colleges for the city with most players - {cityName}")
# plt.show()




#Race of the players
race_players=player_master.groupby("race").size().reset_index(name="number_of_players")
race_dictionary=race_players.to_dict('list')
colors = sns.color_palette("Paired")
explode = [0.1,0.1,0.1,0.1]
plt.pie(race_dictionary["number_of_players"],labels=race_dictionary["race"],autopct = '%0.2f%%',explode=explode,colors=colors)
plt.show()
