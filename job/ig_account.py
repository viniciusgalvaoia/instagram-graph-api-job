from ig_helpers import build_url, request_data


# Account id, ig_id, name, followers_count, follows_count, impressions,reach and profile_views,
#   media_count, biography, website
def get_account_info(base, node, access_token):
    parameters = (
        f"/?fields=id%2Cig_id%2Cusername%2Cname%2Cfollowers_count%2Cfollows_count%2Cmedia_count%2Cbiography"
        f"%2Cwebsite&access_token={access_token} "
    )
    url = build_url(base, node, parameters)
    return request_data(url)


# Account email_contacts,follower_count (new followers each day),get_directions_clicks,impressions,
#   phone_call_clicks,reach, profile_views,text_message_clicks,website_click
def get_day_account_metrics(base, node, access_token):
    parameters = (
        f"/insights?metric=email_contacts,follower_count,get_directions_clicks,impressions,"
        f"phone_call_clicks,reach,profile_views,text_message_clicks,website_clicks&period=day"
        f"&access_token={access_token}"
    )
    url = build_url(base, node, parameters)
    return request_data(url)


# Account audience_city,audience_country,audience_gender_age,audience_locale,online_followers
def get_lifetime_account_metrics(base, node, access_token):
    parameters = (
        f"/insights?metric=audience_city,audience_country,audience_gender_age,audience_locale,online_followers"
        f"&period=lifetime"
        f"&access_token={access_token}"
    )
    url = build_url(base, node, parameters)
    return request_data(url)
