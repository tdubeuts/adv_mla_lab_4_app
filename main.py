timedelta                = st.slider("timedelta", 0, 750, 340)
n_tokens_title           = st.slider("n_tokens_title", 0, 25, 10)
n_tokens_content         = st.slider("n_tokens_content", 0, 9000, 540)
n_unique_tokens          = st.slider("n_unique_tokens", 0., 800., 0.5)
n_non_stop_words         = st.slider("n_non_stop_words", 0, 1100, 1)
n_non_stop_unique_tokens = st.slider("n_non_stop_unique_tokens", 0., 650., 1.0)
num_hrefs                = st.slider("num_hrefs", 0, 350, 10)
num_self_hrefs           = st.slider("num_self_hrefs", 0, 150, 4)
num_imgs                 = st.slider("num_imgs", 0, 150, 10)
num_videos               = st.slider("num_videos", 0, 100, 4)

average_token_length = st.slider("average_token_length", 0., 9., 5.)
num_keywords         = st.slider("num_keywords", 1., 10., 0.5)

data_channel_is_lifestyle     = st.slider("data_channel_is_lifestyle", 0, 1, 0)
data_channel_is_entertainment = st.slider("data_channel_is_entertainment", 0, 1, 0)
data_channel_is_bus           = st.slider("data_channel_is_bus", 0, 1, 0)
data_channel_is_socmed        = st.slider("data_channel_is_socmed", 0, 1, 0)
data_channel_is_tech          = st.slider("data_channel_is_tech", 0, 1, 0)
data_channel_is_world         = st.slider("data_channel_is_world", 0, 1, 0)

kw_min_min = st.slider("kw_min_min", -1, 400, 50)
kw_max_min = st.slider("kw_max_min", 0, 300000, 3500)
kw_avg_min = st.slider("kw_avg_min", 0, 45000, 100)
kw_min_max = st.slider("kw_min_max", 0, 900000, 3500)
kw_max_max = st.slider("kw_max_max", 0, 900000, 3500)
kw_avg_max = st.slider("kw_avg_max", 0, 900000, 3500)
kw_min_avg = st.slider("kw_min_avg", -1, 4000, 50)
kw_max_avg = st.slider("kw_max_avg", 0, 300000, 3500)
kw_avg_avg = st.slider("kw_avg_avg", 0, 45000, 100)

self_reference_min_shares  = st.slider("self_reference_min_shares", 0, 900000, 3500)
self_reference_max_shares  = st.slider("self_reference_max_shares", 0, 900000, 3500)
self_reference_avg_sharess = st.slider("self_reference_avg_sharess", 0, 900000, 3500)

weekday_is_monday    = st.slider("weekday_is_monday", 0, 1, 0)
weekday_is_tuesday   = st.slider("weekday_is_tuesday", 0, 1, 0)
weekday_is_wednesday = st.slider("weekday_is_wednesday", 0, 1, 0)
weekday_is_thursday  = st.slider("weekday_is_thursday", 0, 1, 0)
weekday_is_friday    = st.slider("weekday_is_friday", 0, 1, 0)
weekday_is_saturday  = st.slider("weekday_is_saturday", 0, 1, 0)
weekday_is_sunday    = st.slider("weekday_is_sunday", 0, 1, 0)
is_weekend           = st.slider("is_weekend", 0, 1, 0)

LDA_00 = st.slider("LDA_00", 0, 1, 0)
LDA_01 = st.slider("LDA_01", 0, 1, 0)
LDA_02 = st.slider("LDA_02", 0, 1, 0)
LDA_03 = st.slider("LDA_03", 0, 1, 0)
LDA_04 = st.slider("LDA_04", 0, 1, 0)

global_subjectivity        = st.slider("global_subjectivity", 0., 1., 0.)
global_sentiment_polarity  = st.slider("global_sentiment_polarity", -1., 1., 0.)
global_rate_positive_words = st.slider("global_rate_positive_words", 0., 1., 0.)
global_rate_negative_words = st.slider("global_rate_negative_words", 0., 1., 0.)

rate_positive_words   = st.slider("rate_positive_words", 0., 1., 0.)
rate_negative_words   = st.slider("rate_negative_words", 0., 1., 0.)
avg_positive_polarity = st.slider("avg_positive_polarity", 0., 1., 0.)
min_positive_polarity = st.slider("min_positive_polarity", 0., 1., 0.)
max_positive_polarity = st.slider("max_positive_polarity", 0., 1., 0.)

avg_negative_polarity  = st.slider("avg_negative_polarity", -1., 0., 0.)
min_negative_polarity  = st.slider("min_negative_polarity", -1., 0., 0.)
max_negative_polarity  = st.slider("max_negative_polarity", -1., 0., 0.)

title_subjectivity   = st.slider("title_subjectivity", 0., 1., 0.)
title_sentiment_polarity  = st.slider("title_sentiment_polarity", -1., 1., 0.)
abs_title_subjectivity   = st.slider("abs_title_subjectivity", 0., 0.5, 0.)
abs_title_sentiment_polarity   = st.slider("abs_title_sentiment_polarity", 0., 1., 0.)

data = {
    'timedelta': [timedelta],
    'n_tokens_title': [n_tokens_title],
    'n_tokens_content': [n_tokens_content],
    'n_unique_tokens': [n_unique_tokens],
    'n_non_stop_words': [n_non_stop_words],
    'n_non_stop_unique_tokens': [n_non_stop_unique_tokens],
    'num_hrefs': [num_hrefs],
    'num_self_hrefs': [num_self_hrefs],
    'num_imgs': [num_imgs],
    'num_videos': [num_videos],
    'average_token_length': [average_token_length],
    'num_keywords': [num_keywords],
    'data_channel_is_lifestyle': [data_channel_is_lifestyle],
    'data_channel_is_entertainment': [data_channel_is_entertainment],
    'data_channel_is_bus': [data_channel_is_bus],
    'data_channel_is_socmed': [data_channel_is_socmed],
    'data_channel_is_tech': [data_channel_is_tech],
    'data_channel_is_world': [data_channel_is_world],
    'kw_min_min': [kw_min_min],
    'kw_max_min': [kw_max_min],
    'kw_avg_min': [kw_avg_min],
    'kw_min_max': [kw_min_max],
    'kw_max_max': [kw_max_max],
    'kw_avg_max': [kw_avg_max],
    'kw_min_avg': [kw_min_avg],
    'kw_max_avg': [kw_max_avg],
    'kw_avg_avg': [kw_avg_avg],
    'self_reference_min_shares': [self_reference_min_shares],
    'self_reference_max_shares': [self_reference_max_shares],
    'self_reference_avg_sharess': [self_reference_avg_sharess],
    'weekday_is_monday': [weekday_is_monday],
    'weekday_is_tuesday': [weekday_is_tuesday],
    'weekday_is_wednesday': [weekday_is_wednesday],
    'weekday_is_thursday': [weekday_is_thursday],
    'weekday_is_friday': [weekday_is_friday],
    'weekday_is_saturday': [weekday_is_saturday],
    'weekday_is_sunday': [weekday_is_sunday],
    'is_weekend': [is_weekend],
    'LDA_00': [LDA_00],
    'LDA_01': [LDA_01],
    'LDA_02': [LDA_02],
    'LDA_03': [LDA_03],
    'LDA_04': [LDA_04],
    'global_subjectivity': [global_subjectivity],
    'global_sentiment_polarity': [global_sentiment_polarity],
    'global_rate_positive_words': [global_rate_positive_words],
    'global_rate_negative_words': [global_rate_negative_words],
    'rate_positive_words': [rate_positive_words],
    'rate_negative_words': [rate_negative_words],
    'avg_positive_polarity': [avg_positive_polarity],
    'min_positive_polarity': [min_positive_polarity],
    'max_positive_polarity': [max_positive_polarity],
    'avg_negative_polarity': [avg_negative_polarity],
    'min_negative_polarity': [min_negative_polarity],
    'max_negative_polarity': [max_negative_polarity],
    'title_subjectivity': [max_negative_polarity],
    'title_sentiment_polarity': [title_sentiment_polarity],
    'abs_title_subjectivity': [abs_title_subjectivity],
    'abs_title_sentiment_polarity': [abs_title_sentiment_polarity],
}

if st.button("Predict"):
    df = pd.DataFrame(data)
    proba = model.predict(scaler.transform(df))
    st.write(f"Prediction: {proba}")