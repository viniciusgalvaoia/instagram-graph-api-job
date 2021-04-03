from ig_helpers import build_url, request_data


# Stories id
def get_stories_id(base, node, access_token):
    parameters = f"/stories?access_token={access_token}"
    url = build_url(base, node, parameters)
    return request_data(url)


# Media id,like_count,comments_count,media_type,media_url,owner,thumbnail_url
def get_media_id(base, node, access_token):
    parameters = f"/media?access_token={access_token}"
    url = build_url(base, node, parameters)
    return request_data(url)


# id,like_count,comments_count,media_type,media_url,owner,thumbnail_url,timestamp,username
def get_media_info(base, media_id_list, access_token):
    att_list = []
    parameters = (
        f"/?fields=id,like_count,comments_count,media_type,media_url,owner,thumbnail_url,"
        f"timestamp,username"
        f"&access_token={access_token} "
    )
    for media_id in media_id_list:
        media_node = f"/{media_id}"
        url = build_url(base, media_node, parameters)
        att_list.append(request_data(url))
    return att_list


# media engagement, impressions, reach,saved and video_views
def get_media_metrics(base, media_id_list, access_token):
    metrics_list = []
    parameters = f"/insights?metric=engagement,impressions,reach,saved&access_token={access_token}"
    for media_id in media_id_list:
        media_node = f"/{media_id}"
        url = build_url(base, media_node, parameters)
        metrics_list.append(request_data(url))
    return metrics_list


# comments text
def get_media_comments(base, media_id_list, access_token):
    metrics_list = []
    parameters = f"/comments?access_token={access_token}"
    for media_id in media_id_list:
        media_node = f"/{media_id}"
        url = build_url(base, media_node, parameters)
        metrics_list.append(request_data(url))
    return metrics_list


# exits,impressions,reach,replies,taps_forward,taps_back
def get_stories_metrics(base, media_id_list, access_token):
    metrics_list = []
    parameters = f"/insights?metric=exits,impressions,reach,replies,taps_forward,taps_back&access_token={access_token}"
    for media_id in media_id_list:
        media_node = f"/{media_id}"
        url = build_url(base, media_node, parameters)
        metrics_list.append(request_data(url))
    return metrics_list
