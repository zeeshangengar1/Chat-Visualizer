from urlextract import URLExtract
from collections import Counter
import pandas as pd
from wordcloud import WordCloud

stop_words=[".", "..", "...", "?", "-", "--", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "aadi", "aaj", "aap", "aapne", "aata", "aati", "aaya", "aaye", "ab", "abbe", "abbey", "abe", "abhi", "able", "about", "above", "accha", "according", "accordingly", "acha", "achcha", "across", "actually", "after", "afterwards", "again", "against", "agar", "ain", "aint", "ain't", "aisa", "aise", "aisi", "alag", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "andar", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "ap", "apan", "apart", "apna", "apnaa", "apne", "apni", "appear", "are", "aren", "arent", "aren't", "around", "arre", "as", "aside", "ask", "asking", "at", "aur", "avum", "aya", "aye", "baad", "baar", "bad", "bahut", "bana", "banae", "banai", "banao", "banaya", "banaye", "banayi", "banda", "bande", "bandi", "bane", "bani", "bas", "bata", "batao", "bc", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "best", "better", "between", "beyond", "bhai", "bheetar", "bhi", "bhitar", "bht", "bilkul", "bohot", "bol", "bola", "bole", "boli", "bolo", "bolta", "bolte", "bolti", "both", "brief", "bro", "btw", "but", "by", "came", "can", "cannot", "cant", "can't", "cause", "causes", "certain", "certainly", "chahiye", "chaiye", "chal", "chalega", "chhaiye", "clearly", "c'mon", "com", "come", "comes", "could", "couldn", "couldnt", "couldn't", "d", "de", "dede", "dega", "degi", "dekh", "dekha", "dekhe", "dekhi", "dekho", "denge", "dhang", "di", "did", "didn", "didnt", "didn't", "dijiye", "diya", "diyaa", "diye", "diyo", "do", "does", "doesn", "doesnt", "doesn't", "doing", "done", "dono", "dont", "don't", "doosra", "doosre", "down", "downwards", "dude", "dunga", "dungi", "during", "dusra", "dusre", "dusri", "dvaara", "dvara", "dwaara", "dwara", "each", "edu", "eg", "eight", "either", "ek", "else", "elsewhere", "enough", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "far", "few", "fifth", "fir", "first", "five", "followed", "following", "follows", "for", "forth", "four", "from", "further", "furthermore", "gaya", "gaye", "gayi", "get", "gets", "getting", "ghar", "given", "gives", "go", "goes", "going", "gone", "good", "got", "gotten", "greetings", "guys", "h","ha","haa","shi","sb","hogya""haan", "had", "hadd", "hadn", "hadnt", "hadn't", "hai", "hain", "hamara", "hamare", "hamari", "hamne", "han", "happens", "har", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "havent", "haven't", "having", "he", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself", "he's", "hi", "him", "himself", "his", "hither", "hm", "hmm", "ho", "hoga", "hoge", "hogi", "hona", "honaa", "hone", "honge", "hongi", "honi", "hopefully", "hota", "hotaa", "hote", "hoti", "how", "howbeit", "however", "hoyenge", "hoyengi", "hu", "hua", "hue", "huh", "hui", "hum", "humein", "humne", "hun", "huye", "huyi", "i", "i'd", "idk", "ie", "if", "i'll", "i'm", "imo", "in", "inasmuch", "inc", "inhe", "inhi", "inho", "inka", "inkaa", "inke", "inki", "inn", "inner", "inse", "insofar", "into", "inward", "is", "ise", "isi", "iska", "iskaa", "iske", "iski", "isme", "isn", "isne", "isnt", "isn't", "iss", "isse", "issi", "isski", "it", "it'd", "it'll", "itna", "itne", "itni", "itno", "its", "it's", "itself", "ityaadi", "ityadi", "i've", "ja", "jaa", "jab", "jabh", "jaha", "jahaan", "jahan", "jaisa", "jaise", "jaisi", "jata", "jayega", "jidhar", "jin", "jinhe", "jinhi", "jinho", "jinhone", "jinka", "jinke", "jinki", "jinn", "jis", "jise", "jiska", "jiske", "jiski", "jisme", "jiss", "jisse", "jitna", "jitne", "jitni", "jo", "just", "jyaada", "jyada", "k", "ka", "kaafi", "kab", "kabhi", "kafi", "kaha", "kahaa", "kahaan", "kahan", "kahi", "kahin", "kahte", "kaisa", "kaise", "kaisi", "kal", "kam", "kar", "kara", "kare", "karega", "karegi", "karen", "karenge", "kari", "karke", "karna", "karne", "karni", "karo", "karta", "karte", "karti", "karu", "karun", "karunga", "karungi", "kaun", "kaunsa", "kayi", "kch", "ke", "keep", "keeps", "keh", "kehte", "kept", "khud", "ki", "kin", "kine", "kinhe", "kinho", "kinka", "kinke", "kinki", "kinko", "kinn", "kino", "kis", "kise", "kisi", "kiska", "kiske", "kiski", "kisko", "kisliye", "kisne", "kitna", "kitne", "kitni", "kitno", "kiya", "kiye", "know", "known", "knows", "ko", "koi", "kon", "konsa", "koyi", "krna", "krne", "kuch", "kuchch", "kuchh", "kul", "kull", "kya", "kyaa", "kyu", "kyuki", "kyun", "kyunki", "lagta", "lagte", "lagti", "last", "lately", "later", "le", "least", "lekar", "lekin", "less", "lest", "let", "let's", "li", "like", "liked", "likely", "little", "liya", "liye", "ll", "lo", "log", "logon", "lol", "look", "looking", "looks", "ltd", "lunga", "m", "maan", "maana", "maane", "maani", "maano", "magar", "mai", "main", "maine", "mainly", "mana", "mane", "mani", "mano", "many", "mat", "may", "maybe", "me", "mean", "meanwhile", "mein", "mera", "mere", "merely", "meri", "might", "mightn", "mightnt", "mightn't", "mil", "mjhe", "more", "moreover", "most", "mostly", "much", "mujhe", "must", "mustn", "mustnt", "mustn't", "my", "myself", "na", "naa", "naah", "nahi", "nahin", "nai", "name", "namely", "nd", "ne", "near", "nearly", "necessary", "neeche", "need", "needn", "neednt", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "nhi", "nine", "no", "nobody", "non", "none", "noone", "nope", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "par", "pata", "pe", "pehla", "pehle", "pehli", "people", "per", "perhaps", "phla", "phle", "phli", "placed", "please", "plus", "poora", "poori", "provides", "pura", "puri", "q", "que", "quite", "raha", "rahaa", "rahe", "rahi", "rakh", "rakha", "rakhe", "rakhen", "rakhi", "rakho", "rather", "re", "really", "reasonably", "regarding", "regardless", "regards", "rehte", "rha", "rhaa", "rhe", "rhi", "ri", "right", "s", "sa", "saara", "saare", "saath", "sab", "sabhi", "sabse", "sahi", "said", "sakta", "saktaa", "sakte", "sakti", "same", "sang", "sara", "sath", "saw", "say", "saying", "says", "se", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "shan", "shant", "shan't", "she", "she's", "should", "shouldn", "shouldnt", "shouldn't", "should've", "si", "sir", "sir.", "since", "six", "so", "soch", "some", "somebody", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "still", "sub", "such", "sup", "sure", "t", "tab", "tabh", "tak", "take", "taken", "tarah", "teen", "teeno", "teesra", "teesre", "teesri", "tell", "tends", "tera", "tere", "teri", "th", "tha", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "the", "theek", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "theres", "there's", "thereupon", "these", "they", "they'd", "they'll", "they're", "they've", "thi", "thik", "thing", "think", "thinking", "third", "this", "tho", "thoda", "thodi", "thorough", "thoroughly", "those", "though", "thought", "three", "through", "throughout", "thru", "thus", "tjhe", "to", "together", "toh", "too", "took", "toward", "towards", "tried", "tries", "true", "truly", "try", "trying", "tu", "tujhe", "tum", "tumhara", "tumhare", "tumhari", "tune", "twice", "two", "um", "umm", "un", "under", "unhe", "unhi", "unho", "unhone", "unka", "unkaa", "unke", "unki", "unko", "unless", "unlikely", "unn", "unse", "until", "unto", "up", "upar", "upon", "us", "use", "used", "useful", "uses", "usi", "using", "uska", "uske", "usne", "uss", "usse", "ussi", "usually", "vaala", "vaale", "vaali", "vahaan", "vahan", "vahi", "vahin", "vaisa", "vaise", "vaisi", "vala", "vale", "vali", "various", "ve", "very", "via", "viz", "vo", "waala", "waale", "waali", "wagaira", "wagairah", "wagerah", "waha", "wahaan", "wahan", "wahi", "wahin", "waisa", "waise", "waisi", "wala", "wale", "wali", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "we'd", "well", "we'll", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what's", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "where's", "whereupon", "wherever", "whether", "which", "while", "who", "whoever", "whole", "whom", "who's", "whose", "why", "will", "willing", "with", "within", "without", "wo", "woh", "wohi", "won", "wont", "won't", "would", "wouldn", "wouldnt", "wouldn't", "y", "ya", "yadi", "yah", "yaha", "yahaan", "yahan", "yahi", "yahin", "ye", "yeah", "yeh", "yehi", "yes", "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself", "yourselves", "you've", "yup"]
import emoji

extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Name', 'user': '%age'})
    return x,df

def create_wordcloud(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'Group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='black')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'Group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap















