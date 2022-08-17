# import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import helper
chat=sys.argv[1]
if chat is not None:
    df = preprocessor.preprocess(chat)

    user_list = df['user'].unique().tolist()
    user_list.remove('Group_Notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    
    num_messages, words, num_media_messages, num_links = helper.fetch_stats("Overall",df)

    x,new_df = helper.most_busy_users(df)

    with open("files/info.txt", "w") as text_file:
        text_file.writelines("Total messages sent          :          %s \n" % num_messages) 
        text_file.writelines("Total words used in the chat   :          %s  \n" % words) 
        text_file.writelines("Total media links shared     :          %s  \n" % num_media_messages) 
        text_file.writelines("Total links shared          :          %s \n" % num_links) 
        text_file.writelines(" %s \n" % new_df) 

   
    timeline = helper.monthly_timeline("Overall",df)
    fig,ax = plt.subplots()
    ax.plot(timeline['time'], timeline['message'],color='green')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/timeline.jpg",bbox_inches = 'tight')
    
    daily_timeline = helper.daily_timeline("Overall", df)
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/daily_timeline.jpg",bbox_inches = 'tight')
 
    busy_day = helper.week_activity_map("Overall",df)
    fig,ax = plt.subplots()
    ax.bar(busy_day.index,busy_day.values,color='purple')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/busy_day.jpg",bbox_inches = 'tight')
  
    busy_month = helper.month_activity_map("Overall", df)
    
    fig, ax = plt.subplots()
    ax.bar(busy_month.index, busy_month.values,color='orange')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/busy_month.jpg",bbox_inches = 'tight')
    
    user_heatmap = helper.activity_heatmap("Overall",df)
    fig,ax = plt.subplots()
    ax = sns.heatmap(user_heatmap)
    fig.savefig("public/img/user_heatmap.jpg",bbox_inches = 'tight')
    
    fig, ax = plt.subplots()
    ax.bar(x.index, x.values,color='red')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/most_busy_users.jpg",bbox_inches = 'tight')
    
    emoji_df = helper.emoji_helper("Overall",df)

    print("")

    fig,ax = plt.subplots()
    ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
    fig.savefig("public/img/emoji.jpg",bbox_inches = 'tight')
   
    most_common_df = helper.most_common_words("Overall",df)
    fig,ax = plt.subplots()
    ax.bar(most_common_df[0],most_common_df[1],color='blue')
    plt.xticks(rotation='vertical')
    fig.savefig("public/img/most_common_words.jpg",bbox_inches = 'tight')
   
    df_wc = helper.create_wordcloud("Overall",df)
    fig,ax = plt.subplots()
    ax.imshow(df_wc)
    fig.savefig("public/img/wordcloud.jpg", bbox_inches = 'tight')


    
  

  









